import pika

credentials = pika.PlainCredentials(username='sherali.adm', password='**********************')
connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='rmq-test.aamajor.local',credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='RMQ_QaS_02')

channel.basic_publish(exchange='',
                      routing_key='RMQ_QaS_02',
                      body='Hello World!')
print (" [x] Sent 'Hello World!'")
connection.close()