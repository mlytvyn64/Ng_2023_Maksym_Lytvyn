def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def display_table(user_input):
    try:
        user_number = int(user_input)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    print("Number\tDivisors")
    print("---------------------")
    for num in range(1, user_number + 1):
        divisors = [str(i) for i in range(1, num + 1) if num % i == 0]
        print(f"{num}\t{', '.join(divisors)}")

    print("\nPrime Numbers:")
    primes = [str(num) for num in range(2, user_number + 1) if is_prime(num)]
    print(', '.join(primes))

# Get user input
user_input = input("Enter a number: ")

# Display the table and prime numbers
display_table(user_input)
