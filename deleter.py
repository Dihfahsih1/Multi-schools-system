# Define the input and output file paths
input_file = "req.txt"  # Replace with the path to your input file
output_file = "require.txt"  # Replace with the desired output file path

# Open the input file for reading and the output file for writing
with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    # Iterate through each line in the input file
    for line in infile:
        # Split the line at '=='
        parts = line.strip().split("==", 1)
        # Write the part before '==' to the output file
        if len(parts) > 0:
            outfile.write(parts[0] + "\n")

print(f"Characters after '==' removed. Output written to {output_file}")