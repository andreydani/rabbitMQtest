import pika

def main():
    # Conectar ao servidor RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()

    # Declarar uma fila chamada 'hello' (deve ser a mesma do produtor)
    channel.queue_declare(queue='hello')

    # Função de callback para processar mensagens
    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")

    # Consumir mensagens da fila 'hello'
    channel.basic_consume(queue='hello',
                          on_message_callback=callback,
                          auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == "__main__":
    main()
