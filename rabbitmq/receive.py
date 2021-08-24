#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

#idempotent>only 1
channel.queue_declare(queue='hello')

#view queue message
#sudo rabbitmqctl list_queues

#to recieve message   callback---subscribe---> queue

#define callback to print message
def callback(ch,method,properties,body):
    print(" [x] recieved %r" %body)

#tell rabbitMQ this recieves for hello
channel.basic_consume(queue='hello',
                      auto_ack=True,
                      on_message_callback=callback)

#infinity
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()