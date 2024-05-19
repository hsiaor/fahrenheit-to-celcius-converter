import celcius_client

get_celcius = celcius_client.CelciusClient()

response = get_celcius.call(32)
print("Temperature in Celcius:",str(response))