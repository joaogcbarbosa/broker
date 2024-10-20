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

    def _deliver_messages(self, message: str) -> str:
        return message

    def run(self):
        while True:
            print(self.queues["Sports"].qsize())
            print(self._deliver_messages(self.queues["Sports"].get()))
            sleep(3)


class Publisher(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        sports_counter = news_counter = tech_counter = 1
        while True:
            topic_choice = choice(TOPICS)
            match topic_choice:
                case "Sports":
                    broker.queues["Sports"].put(f"{topic_choice} {sports_counter}")
                    sports_counter += 1
                # case "News":
                #     broker.queues["News"].put(f"{topic_choice} {news_counter}")
                #     news_counter += 1
                # case "Tech":
                #     broker.queues["Tech"].put(f"{topic_choice} {tech_counter}")
                #     tech_counter += 1
            sleep(2)


class Subscriber(Process):
    def __init__(self, topic):
        Process.__init__(self)
        self._topic = topic

    @property
    def topic(self):
        return self._topic

    def run(self):
        while True:
            if self.topic == "Sports":
                print("Listening Sports every 2 seconds")
                sleep(2)
            elif self.topic == "Tech":
                print("Listening Tech every 1 second")
                sleep(1)


if __name__ == "__main__":
    # publisher = Publisher()
    # broker = Broker()
    sports_subscriber = Subscriber(topic="Sports")
    # tech_subscriber = Subscriber(topic="Tech")
    sports_subscriber.start()
    tech_subscriber.start()

    # publisher.start()
    # broker.start()
