import time

def farenheit_to_celcius(num):
	celcius = (farenheit - 32) * 5 / 9
	# print("Temperature in Celsius:", round(celcius,3))
	return round(celcius,3)

# farenheit = 50
# farenheit_to_celcius(farenheit)

while True:
	time.sleep(1)
	with open("farenheit-to-celcius.txt", r) as file:
		farenheit = file.readlines()
        farenheit_to_celcius(farenheit)
	
		