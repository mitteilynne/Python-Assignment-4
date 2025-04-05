def read_modify_and_write_file():
    # Ask the user for the input filename
    input_filename = input("Please enter the input filename: ")
    
    # Ask the user for the output filename
    output_filename = input("Please enter the output filename: ")
    
    try:
        # Attempt to open the input file for reading
        with open(input_filename, 'r') as file:
            content = file.read()
        
        # Modify the content (e.g., convert content to uppercase)
        modified_content = content.upper()

        # Attempt to open the output file for writing the modified content
        with open(output_filename, 'w') as file:
            file.write(modified_content)

        print(f"Content from {input_filename} has been successfully modified and saved to {output_filename}.")

    except FileNotFoundError:
        print(f"Error: The file {input_filename} was not found.")
    except IOError as e:
        print(f"Error: There was a problem reading or writing to the file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
read_modify_and_write_file()
