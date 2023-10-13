input_str = input("Enter items separated by space: ")

elements = input_str.split()

unique_elements = set(elements)

unique_list = list(unique_elements)

print("Unique elements:", unique_list)
