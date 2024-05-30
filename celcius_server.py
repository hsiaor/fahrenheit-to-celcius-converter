#server program
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.queue_declare(queue='celcius_queue')

def fahrenheit_to_celcius(fahrenheit):
    celcius = round((fahrenheit - 32) * 5/9)
    return celcius

def on_request(ch, method, props, body):
    n = int(body)

    print(f" [.] celcius({n})")
    response = fahrenheit_to_celcius(n)

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id = \
                                                         props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='celcius_queue', on_message_callback=on_request)

print(" [x] Awaiting celcius conversion requests")
channel.start_consuming()
