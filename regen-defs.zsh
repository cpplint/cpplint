#!/bin/zsh

# Input the path of cpplint here
cpplint="$HOME/Documents/cpplint/cpplint.py"

cd samples/ || exit 74  # EX_IOERROR

# Loop through all .def files in the given directories
folders=(${(f)"$(cat)"})
for folder in $folders; do
  cd "$folder-sample/" || exit 66  # EX_NOINPUT
  for file in ./*.def; do
    if [[ ! -s "$file" ]]; then
      echo "Skipping empty file: $file"
      continue
    fi
    echo "Processing $file..."

    # Extract the command from the first line of the file
    cmd=$(head -n 1 "$file")

    # Create temporary files for stdout and stderr
    stdout_file=$(mktemp)
    stderr_file=$(mktemp)

    # Execute the command and capture stdout and stderr
    uv run "$cpplint" $cmd > "$stdout_file" 2> "$stderr_file"
    ret_code=$?

    # Count the number of lines in stdout
    (( num_lines=$(wc -l < "$stdout_file") + 1 ))

    # Overwrite the original definition file
    {
      echo "$cmd"
      echo "$ret_code"
      echo "$num_lines"
      cat "$stdout_file"
      echo
      cat "$stderr_file"
      echo
    } > "$file"

    # Clean up temporary files
    rm "$stdout_file" "$stderr_file"
  done
  cd ..
done
