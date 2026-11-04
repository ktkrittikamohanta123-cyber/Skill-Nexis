# Assignment 1: Temperature Converter
# Convert Celsius to Fahrenheit and Fahrenheit to Celsius using functions.

def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32


def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9


print("Temperature Converter")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = int(input("Enter your choice: "))

if choice == 1:
    celsius = float(input("Enter temperature in Celsius: "))
    result = celsius_to_fahrenheit(celsius)
    print("Temperature in Fahrenheit:", result)

elif choice == 2:
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    result = fahrenheit_to_celsius(fahrenheit)
    print("Temperature in Celsius:", result)

else:
    print("Invalid choice")
