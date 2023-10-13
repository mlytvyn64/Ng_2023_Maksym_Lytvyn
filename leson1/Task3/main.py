def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

print("Choose convert")
print("1. Celsium in Fanringeit")
print("2. Faringeit in Celsium")

choice = input("Your varient (1/2): ")

if choice == '1':
    celsius = float(input("Write temp in Celsium: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius} temp in Celsian = {fahrenheit} temp in Faringeit")
elif choice == '2':
    fahrenheit = float(input("Write temp in Faringeit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit} temp in Faringeit {celsius} temp in Celsia")
else:
    print("ERRORR")