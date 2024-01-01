def remove_integers_from_start(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as infile, \
             open(output_file, 'w', encoding='utf-8') as outfile:

            for line in infile:
                # Remove integers from the first 8 characters of the line
                cleaned_line = ''.join(char if not char.isdigit() else '' for char in line[:8]) + line[8:]
                outfile.write(cleaned_line)

        print(f"Integers removed from the first 8 characters of each line. Result saved to {output_file}")

    except FileNotFoundError:
        print("Input file not found.")

if __name__ == "__main__":
    input_file = "input.txt"  # Replace with your input file name
    output_file = "output.txt"  # Replace with your output file name
    remove_integers_from_start(input_file, output_file)
