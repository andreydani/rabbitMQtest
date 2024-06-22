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

    try:
        channel = connection.channel()

        # Declarar uma fila chamada 'hello'
        channel.queue_declare(queue='hello')
    except Exception as e:
        print('Failed to initialize rabbitMQ channel' + str(e))

    # Função de callback para processar mensagens
    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")

    # Consumir mensagens da fila 'hello'
    try:
        channel.basic_consume(queue='hello',
                          on_message_callback=callback,
                          auto_ack=True)
    except Exception as e:
        print('Failed to consume ' + str(e))

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == "__main__":
    main()
