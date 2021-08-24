#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

##connected to a broker on local machine

##if location exists (otherwise dropped)
channel.queue_declare(queue='hello')

##define exchange prior to entering queue
##queue name defined by routing_key
channel.basic_publish(exchange='', routing_key='hello',body='Hello World!')
print(" [x] Sent 'Hello World!'")

##to confirm network buffer is flushed
connection.close()


#default broker size needed=200mb (disk_free_limit)
