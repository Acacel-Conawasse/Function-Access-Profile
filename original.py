def process_file(file_path):
    # Attempt to open and read the file
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

    # Filtering lines that start with '#'
    processed_lines = [line for line in lines if line.startswith('#')]

    # Debugging: Print the number of lines processed
    print(f"Total lines read: {len(lines)}")
    print(f"Lines kept that start with '#': {len(processed_lines)}")

    return processed_lines

# Specify the path to the original file
file_path = 'Original.txt'

# Process the file
result_lines = process_file(file_path)

# Check if there are any lines to write
if result_lines:
    # Write the result to a new file
    with open('filtered_lines.txt', 'w') as file:
        file.writelines(result_lines)
    print("Filtered lines have been written to 'filtered_lines.txt'.")
else:
    print("No lines starting with '#' were found or an error occurred.")
