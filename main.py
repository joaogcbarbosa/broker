from threading import Thread
from multiprocessing import Queue, Process
from random import choice
from time import sleep

TOPICS = ["Sports", "News", "Tech"]
TOPICS = ["Sports"]

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
        sports_counter = 1
        while True:
            topic_choice = choice(TOPICS)
            match topic_choice:
                case "Sports":
                    msg = f"{topic_choice} {sports_counter}"
                    broker.queues["Sports"].put(msg)
                    sports_counter += 1
                    broker.queues["Sports"].put(None)
            sleep(2)


class Subscriber(Process):
    def __init__(self, topic):
        Process.__init__(self)
        self._topic: str = topic

    @property
    def topic(self):
        return self._topic
    
    def get_message(self, topic: str):
        while True:
            item = broker.queues[topic].get()
            if item is None:
                break
            print(f"Consumindo {item}")

    def run(self):
        """
            Get messages from broker every 3 seconds.
        """
        while True:
            self.get_message(self.topic)
            sleep(3)


if __name__ == "__main__":
    publisher = Publisher()
    broker = Broker()
    sports_subscriber = Subscriber(topic="Sports")

    sports_subscriber.start()
    publisher.start()
    broker.start()
