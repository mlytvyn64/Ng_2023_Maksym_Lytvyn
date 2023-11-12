def count_numbers(input_list):
    number_count = 0

    for item in input_list:
        if isinstance(item, (int, float)):
            number_count += 1

    return number_count

# Get user input
user_input = input("Enter the elements of the list separated by space: ")

# Convert the input string into a list by splitting elements at spaces
input_list = user_input.split()

# Convert each element of the list to a number (if possible)
input_list = []
for item in user_input.split():
    try:
        num = float(item)
        input_list.append(num)
    except ValueError:
        pass

# Call the count_numbers function
result = count_numbers(input_list)

# Display the result
print(f"Number of numbers in the list: {result}")