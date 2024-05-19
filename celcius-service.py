import os


# Read the Fahrenheit value from the file
with open('fahrenheit-to-celcius.txt', 'r') as file:
    fahrenheit = float(file.read().strip())

# Convert Fahrenheit to Celsius
celsius = round((fahrenheit - 32) * 5/9)

# Write the Celsius value back to the file
with open('fahrenheit-to-celcius.txt', 'w') as file:
    file.write(str(celsius))
