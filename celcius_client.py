#!/usr/bin/env python
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


get_celcius = CelciusClient()


def main():
    """
    Main function that runs the user interface loop.
    """
    while True:
        user_input = input("Enter temperature in Fahrenheit: ")

        if user_input.isdigit():
            response = get_celcius.call(user_input)
            print("Temperature in Celcius:",str(response))
        else:
            print("Unknown option. Please try again.")


if __name__ == "__main__":
    main()
    