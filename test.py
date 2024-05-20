import celcius_client

get_celcius = celcius_client.CelciusClient()

fahrenheit = 32

response = get_celcius.call(fahrenheit)
print("Temperature in Celcius:",str(response))
