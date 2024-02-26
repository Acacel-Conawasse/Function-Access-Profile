# Function to read file contents and strip trailing whitespace
def read_file_contents_strip_whitespace(file_path):
    with open(file_path, 'r') as file:
        # Strip trailing whitespace from each line
        return [line.rstrip() for line in file.readlines()]

# Read contents of both files, stripping trailing whitespace
data_validation1_lines = read_file_contents_strip_whitespace('DataValidation1.txt')
data_validation2_lines = read_file_contents_strip_whitespace('DataValidation2.txt')

# Convert lines to sets and find differences
differences = set(data_validation1_lines).symmetric_difference(set(data_validation2_lines))

# Write differences to MissingLines.txt
with open('MissingLines.txt', 'w') as file:
    for line in sorted(differences):
        file.write(line + '\n')  # Add newline character to each line

print("Differences written to MissingLines.txt.")
