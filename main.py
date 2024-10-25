from multiprocessing import Process, Queue
from random import choice
from threading import Thread
from time import sleep

TOPICS = ["Sports", "News", "Tech"]


class Subscriber(Process):
    def __init__(self, name, topics, queue):
        Process.__init__(self)
        self.__name = name
        self.__topics = topics
        self.__messages = []
        self.__queue = queue

    @property
    def name(self):
        return self.__name

    @property
    def topics(self):
        return self.__topics

    @property
    def messages(self):
        return self.__messages

    @property
    def queue(self):
        return self.__queue

    def append_message(self, msg):
        self.__messages.append(msg)

    def run(self):
        """
        Se a fila real não estiver vazia, tira a mensagem dela
        Se a mensagem já não estiver na lista de mensagens, é posta
        Mostra a mensagem no terminal
        """
        while True:
            if not self.queue.empty():
                msg = self.queue.get()
                if msg not in self.messages:
                    self.append_message(msg)
            print(f"{self.name} messages: {self.messages}")
            sleep(3)


class Broker(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.__queues = {t: [] for t in TOPICS}
        self.__subscribers = []

    @property
    def queues(self):
        return self.__queues

    @property
    def subscribers(self):
        return self.__subscribers

    def push_to_queue(self, topic, msg):
        self.queues[topic].append(msg)

    def subscribe(self, sub, queue):
        self.subscribers.append({"subscriber": sub, "queue": queue})

    def run(self):
        while True:
            """
            Varre a lista de subscribers.
            Se o subscriber estiver de fato inscrito para receber mensagem de algum tópico, varre esses tópicos
            E itera sob a "fila" de mensagens, botando cada mensagem na fila real.
            """
            for s in self.subscribers:
                subscriber = s["subscriber"]
                queue = s["queue"]
                if subscriber.topics:
                    for topic in subscriber.topics:
                        for msg in self.queues[topic]:
                            queue.put(f"{subscriber.name} recebeu {msg}")
            sleep(1)


class Publisher(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        """
        Gera uma mensagem de assunto aleatório (entre Sports, News e Tech) e põe na "fila" a cada 0,5 segundos
        """
        sports_counter = news_counter = tech_counter = 0
        while True:
            topic_choice = choice(TOPICS)
            if topic_choice == "Sports":
                sports_counter += 1
                msg = f"Mensagem {topic_choice} {sports_counter}"
            elif topic_choice == "News":
                news_counter += 1
                msg = f"Mensagem {topic_choice} {news_counter}"
            elif topic_choice == "Tech":
                tech_counter += 1
                msg = f"Mensagem {topic_choice} {tech_counter}"
            else:
                raise RuntimeError
            broker.push_to_queue(topic_choice, msg)
            sleep(0.5)


if __name__ == "__main__":
    broker = Broker()
    publisher = Publisher()

    # Cria filas para cada subscriber
    queue_1 = Queue()
    queue_2 = Queue()
    queue_3 = Queue()
    queue_4 = Queue()

    # Cria os subscribers
    subscriber_1 = Subscriber(name="João", topics=["Sports", "Tech"], queue=queue_1)
    subscriber_2 = Subscriber(name="Gustavo", topics=["Sports"], queue=queue_2)
    subscriber_3 = Subscriber(name="Rafael", topics=None, queue=queue_3)
    subscriber_4 = Subscriber(name="Tiago", topics=["News"], queue=queue_4)

    # Inscreve os subscribers no broker com suas respectivas filas
    broker.subscribe(subscriber_1, queue_1)
    broker.subscribe(subscriber_2, queue_2)
    broker.subscribe(subscriber_3, queue_3)
    broker.subscribe(subscriber_4, queue_4)

    # Inicia os processos
    broker.start()
    publisher.start()
    subscriber_1.start()
    subscriber_2.start()
    subscriber_3.start()
    subscriber_4.start()
