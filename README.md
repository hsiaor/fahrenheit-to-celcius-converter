# Fahrenheit to Celcius Converter

This microservice converts temperatures from Fahrenheit to Celcius. Use the Client program to request and receive the converted temperature from the Server program.

## Prerequisites

Before you beging, ensure you have the Pika client and RabbitMQ installed and running locally on localhost standard port (5672). For more informatoin, see the [RabbitMQ documentation](https://www.rabbitmq.com/tutorials/tutorial-one-python#prerequisites).

If using the Docker image from the RabbitMQ documentation, you can open a terminal and run:

```
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.13-management
```

## How to programmatically REQUEST and RECEIVE data from the microservice

1. Create a `CelciusClient()` class in the requesting (client) program that has a `call` method to send the request. For example:

    ```py
        #client program
        import pika
        import uuid


        class CelciusClient(object):

            def __init__(self):
                self.connection = pika.BlockingConnection(
                    pika.ConnectionParameters(host='localhost'))

                self.channel = self.connection.channel()

                result = self.channel.queue_declare(queue='', exclusive=True)
                self.callback_queue = result.method.queue

                self.channel.basic_consume(
                    queue=self.callback_queue,
                    on_message_callback=self.on_response,
                    auto_ack=True)

                self.response = None
                self.corr_id = None

            def on_response(self, ch, method, props, body):
                if self.corr_id == props.correlation_id:
                    self.response = body

            def call(self, n):
                self.response = None
                self.corr_id = str(uuid.uuid4())
                self.channel.basic_publish(
                    exchange='',
                    routing_key='rpc_queue',
                    properties=pika.BasicProperties(
                        reply_to=self.callback_queue,
                        correlation_id=self.corr_id,
                    ),
                    body=str(n))
                while self.response is None:
                    self.connection.process_data_events(time_limit=None)
                return int(self.response)


        if __name__ == "__main__":
            """Example test program"""

            get_celcius = CelciusClient()

            while True:
                user_input = input("Enter temperature in Fahrenheit: ")

                if user_input.isdigit():
                    response = get_celcius.call(user_input)
                    print("Temperature in Celcius:",str(response))
                else:
                    print("Unknown option. Please try again.")

    ```

21. Open a terminal and start the Server program by running:

    ```sh
    python celcius_server.py
    ```

3. Open a NEW terminal and start the Client program by running:

    ```sh
    python celcius_client.py
    ```

4. Send a request with Fahrenheit temperature (type: int) to the Server using the example test program:

    1. At the prompt in the Client program terminal, enter the temperature in Fahrenheit.

        ![sample-client-cli](sample-client-cli-call.png)
        
    2. Wait for the microservice to return the temperature in Celcius.

## UML sequence diagram showing how requesting and receiving data works

![UML](sequence-diagram.svg)
