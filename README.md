# rabbitMQtest
Simple test of RabbitMQ in Python

This is simple messaging test for RabbitMQ.

## consumer.py
This script waits for messages.

## producer.py 
This script sends one message and leaves.

Requirements:

* Python
* Erlang/OTP
* RabbitMQ

# Expected results on consumer.py
~~~
python.exe C:\projetos\rabbitMQtest\consumer.py 
 [*] Waiting for messages. To exit press CTRL+C
 [x] Received b'Hello World!'
 [x] Received b'Hello World!'
 [x] Received b'Hello World!'
 [x] Received b'Hello World!'
~~~
# Expected results on producer.py
~~~
python.exe C:\projetos\geolocation\producer.py 
 [x] Sent 'Hello World!'
~~~
