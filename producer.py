import pika
import time

def main():
    # Tentativa de conexão com o RabbitMQ
    connected = False
    while not connected:
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
            connected = True
        except pika.exceptions.AMQPConnectionError:
            print("Aguardando RabbitMQ...")
            time.sleep(5)

    channel = connection.channel()

    # Declarar uma fila chamada 'hello'
    channel.queue_declare(queue='hello')

    # Enviar uma mensagem para a fila 'hello'
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body='Hello World!')

    print(" [x] Sent 'Hello World!'")

    # Fechar a conexão
    connection.close()

if __name__ == "__main__":
    main()
