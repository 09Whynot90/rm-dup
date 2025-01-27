import sys
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

headerName = """
                                        ▄▄                       
                                      ▀███                       
                                        ██                       
▀███▄███▀████████▄█████▄           ▄█▀▀███ ▀███  ▀███ ▀████████▄ 
  ██▀ ▀▀  ██    ██    ██         ▄██    ██   ██    ██   ██   ▀██ 
  ██      ██    ██    ██   █████ ███    ██   ██    ██   ██    ██ 
  ██      ██    ██    ██         ▀██    ██   ██    ██   ██   ▄██ 
▄████▄  ▄████  ████  ████▄        ▀████▀███▄ ▀████▀███▄ ██████▀  
                                                        ██       
                                                      ▄████▄     
                            (by WhyNot..?)
"""

# Print the header with green color
print(Fore.GREEN + Style.BRIGHT + headerName)

# Check for the '-h' argument and display a help message
if '-h' in sys.argv:
    help_message = """
Usage:
  python3 filename.py [-h]
  
Description:
  This script removes duplicate words from a given text file and saves the result to another file.
  
Steps:
  1. Enter name file you wante removes duplicate words (input.txt).
  2. Enter name file to save output (output.txt).
  
  The script processes the input file, removes duplicate words, and writes the unique words to the output file.
"""
    print(Fore.YELLOW + help_message)
    sys.exit()  # Exit the program after displaying help


# Function to remove duplicate words from a file
def remove_duplicate_words_from_large_file(input_file, output_file):
    try:
        # Read all words from the input file
        with open(input_file, 'r', encoding='utf-8') as file:
            words = file.read().split()

        # Remove duplicates while preserving the order
        unique_words = list(dict.fromkeys(words))

        # Write the unique words to the output file
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write("\n".join(unique_words))

        print(Fore.GREEN + Style.BRIGHT +f"Duplicate words removed successfully! Unique words saved in '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Ask the user for input and output file names
input_file_name = input(Fore.BLUE + Style.BRIGHT +"Enter the input file name (with extension): "+ Style.RESET_ALL)
output_file_name = input(Fore.BLUE + Style.BRIGHT +"Enter the output file name (with extension): "+ Style.RESET_ALL)


# Call the function
remove_duplicate_words_from_large_file(input_file_name, output_file_name)
