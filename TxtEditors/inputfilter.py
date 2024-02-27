import csv

# Define the path to the input file
input_file_path = 'C:\\Users\\omalomo3\\Desktop\\FAP\\Function-Access-Profile\\Function-Access-Profile\\TxtEditors\\final.txt'

# Define the path to the output file
output_file_path = 'C:\\Users\\omalomo3\\Desktop\\FAP\\Function-Access-Profile\\Function-Access-Profile\\TxtEditors\\inputfiltered.txt'

# Initialize a list to hold all column values, for 40 columns
columns = [[] for _ in range(40)]  # Adjust the range to match the exact number of columns

# Open the input file and process each line
with open(input_file_path, 'r') as file:
    reader = csv.reader(file, delimiter='\t')  # Adjust the delimiter as necessary
    for row in reader:
        for i, value in enumerate(row):
            if i < len(columns):  # Ensure no index errors
                columns[i].append(value)
            else:
                print(f"Warning: Row with more than expected 40 columns found: {row}")
                break

# Open the output file in write mode
with open(output_file_path, 'w') as file:
    # Iterate through each column
    for column in columns:
        # Write the column's values, delimited by commas, followed by a newline character
        file.write(','.join(column) + '\n')

print(f"Output successfully written to {output_file_path}")
