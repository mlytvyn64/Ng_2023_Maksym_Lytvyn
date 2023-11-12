def extract_vowels(input_string):
    valid_chars = set("aeiouаеёиоуыэюяAEIOUАЕЁИОУЫЭЮЯіІїЇ")
    result = [char for char in input_string if char in valid_chars]
    return ''.join(result)

# Get user input
user_input = input("Enter a string: ")

# Extract and display vowels
vowels_only = extract_vowels(user_input)
print("Vowels only: " + vowels_only)
