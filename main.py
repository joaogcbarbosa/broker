from multiprocessing import Process, Queue
from random import choice
from threading import Thread
from time import sleep

TOPICS = ["Sports", "News", "Tech"]


class Broker(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.queues = {t: Queue() for t in TOPICS}

    def run(self):
        """
        Keeps broker running.
        """
        while True:
            pass


class Publisher(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        """
        Generates a message of a random subject (between Sports, News and Tech) and put it on broker every 2 seconds.
        """
        sports_counter = news_counter = tech_counter = 1
        while True:
            topic_choice = choice(TOPICS)
            match topic_choice:
                case "Sports":
                    msg = f"Mensagem {topic_choice} {sports_counter}"
                    broker.queues["Sports"].put(msg)
                    sports_counter += 1
                    broker.queues["Sports"].put(None)
                case "News":
                    msg = f"Mensagem {topic_choice} {news_counter}"
                    broker.queues["News"].put(msg)
                    news_counter += 1
                    broker.queues["News"].put(None)
                case "Tech":
                    msg = f"Mensagem {topic_choice} {tech_counter}"
                    broker.queues["Tech"].put(msg)
                    tech_counter += 1
                    broker.queues["Tech"].put(None)
            sleep(2)


class Subscriber(Process):
    def __init__(self, name, topics):
        Process.__init__(self)
        self._name: str = name
        self._topics: list[str] | None = topics

    @property
    def topics(self):
        return self._topics

    def get_message(self, topics: list[str]) -> None:
        while True:
            if topics is None:
                continue
            print("#" * 20)
            for t in topics:
                item = broker.queues[t].get()
                if item is None:
                    break
                print(f"{self.name} consumindo {item}")

    def run(self):
        """
        Get messages from broker every 3 seconds.
        """
        while True:
            self.get_message(self.topics)
            sleep(3)


if __name__ == "__main__":
    publisher = Publisher()
    broker = Broker()
    sports_subscriber_1 = Subscriber(name="João", topics=["Sports", "Tech"])
    sports_subscriber_2 = Subscriber(name="Gustavo", topics=["Sports"])
    tech_subscriber_1 = Subscriber(name="Rafael", topics=None)
    news_subscriber_1 = Subscriber(name="Tiago", topics=["News"])

    sports_subscriber_1.start()
    sports_subscriber_2.start()
    tech_subscriber_1.start()
    news_subscriber_1.start()
    broker.start()
    publisher.start()
