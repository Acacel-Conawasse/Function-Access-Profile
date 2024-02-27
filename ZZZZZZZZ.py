# Define paths for the input and output files
# Adjust the paths to include the full directory path from the root or relative to where the script is executed
input_file_path = 'C:/Users/omalomo3/Desktop/FAP/Function-Access-Profile/Function-Access-Profile/Page3.txt'
output_file_path = 'C:/Users/omalomo3/Desktop/FAP/Function-Access-Profile/Function-Access-Profile/FAPPage3.txt'
temp_file_path = 'C:/Users/omalomo3/Desktop/FAP/Function-Access-Profile/Function-Access-Profile/temp_FAPPage3.txt'


# Open the input file and a temporary file to write the modified content
with open(input_file_path, 'r') as input_file, open(temp_file_path, 'w') as temp_file:
    # Initialize a list to store the first column's values
    first_column_values = []
    
    for line in input_file:
        # Split the line into values based on commas
        values = line.strip().split(',')
        
        # Append the first value (first column) to the list
        first_column_values.append(values[0])
        
        # Write the remaining values (excluding the first column) back to the temporary file
        temp_file.write(','.join(values[1:]) + '\n')

# Write the first column's values to the output file, delimited by commas
with open(output_file_path, 'w') as output_file:
    output_file.write('\n'.join(first_column_values))

# Replace the original input file with the modified content from the temporary file
import os
os.remove(input_file_path)  # Remove the original file
os.rename(temp_file_path, input_file_path)  # Rename the temporary file to the original file name

print("Processing complete. First column extracted and original file modified.")
