import os

# Get the file path
file_path = os.path.join(os.path.dirname(__file__), 'temperature.txt')

# Read the Fahrenheit value from the file
with open('farenheit-to-celcius.txt', 'r') as file:
    fahrenheit = float(file.read().strip())

# Convert Fahrenheit to Celsius
celsius = round((fahrenheit - 32) * 5/9)

# Write the Celsius value back to the file
with open('farenheit-to-celcius.txt', 'w') as file:
    file.write(str(celsius))
