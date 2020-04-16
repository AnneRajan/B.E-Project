#!/usr/bin/env python
import pika
import deploy
import json
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='simulations')
channel.queue_declare(queue='results')

def callback(ch, method, properties, body):
    requestParams = json.loads(body.decode('utf-8'))
    os          = int(requestParams[0])
    aoa         = int(requestParams[1])
    pc          = int(requestParams[2])
    se          = int(requestParams[3])
    cn          = int(requestParams[4])
    ma          = int(requestParams[5])
    cs          = int(requestParams[6])
    hac         = int(requestParams[7])
    interest    = requestParams[8]
    cert        = requestParams[9]
    personality = requestParams[10]
    mantech     = requestParams[11]
    leadership  = requestParams[12]
    team        = requestParams[13]
    selfab      = requestParams[14]

    results     = deploy.simulate(os,aoa,pc,se,cn,ma,cs,hac,interest,cert,personality,mantech,leadership,team,selfab)

    # send a message back
    channel.basic_publish(exchange='', routing_key='results', body=json.dumps(results, ensure_ascii=False))
    
# receive message and complete simulation
channel.basic_consume(callback, queue='simulations', no_ack=True)
channel.start_consuming()
