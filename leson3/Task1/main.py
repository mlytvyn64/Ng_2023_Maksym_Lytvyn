import os

def count_characters(filename):
    character_count = {}

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            for char in content:
                if char.isalpha():
                    char_lower = char.lower()
                    if char_lower in character_count:
                        character_count[char_lower] += 1
                    else:
                        character_count[char_lower] = 1
                elif char in character_count:
                    character_count[char] += 1
                else:
                    character_count[char] = 1
    except FileNotFoundError:
        print("File not found. Please enter a valid filename.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return character_count

# Get the filename from the user or use a default filename
file_name = input("Enter the filename (or press Enter to use a default filename): ")

if not file_name:
    file_name = "sample.txt"  

if not os.path.isfile(file_name):
    print(f"File '{file_name}' not found in the local directory.")
else:
    result = count_characters(file_name)

    print("\nCharacter count:")
    for char, count in result.items():
        print(f"{char}: {count}")
