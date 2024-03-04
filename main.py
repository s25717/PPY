# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Prompt the user to enter their name
name = input("Enter your name: ")
surname = input("Enter your surname: ")
age = input("How old are you?: ")

print("Hello,", name +" "+ surname + "!")
print("I know your age, you are " + age + " years old!")

celsius = float(input("Enter temperature in Celsius: "))

# Convert Celsius to Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Print the converted temperature
print("Temperature in Fahrenheit:", fahrenheit)
