from threading import Thread
from multiprocessing import Queue
from random import choice
from time import sleep

TOPICS = ["Sports", "News", "Tech"]
TOPICS = ["Sports", "News"]

class Broker(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.queues = {t: Queue() for t in TOPICS}

    def _deliver_messages(self, topic: str) -> str:
        if topic == "Sports":
            print(self.queues[topic].get())
        elif topic == "News":
            for msg in self.queues[topic]:
                print(msg)
        elif topic == "Tech":
            for msg in self.queues[topic]:
                print(msg)

    def run(self):
        while True:
            print(self.queues["Sports"].get())
            print(self.queues["News"].get())
            # self._deliver_messages(topic="Sports")
            print("waiting")


def publisher_worker() -> None:
    sports_counter = news_counter = tech_counter = 1
    while True:
        topic_choice = choice(TOPICS)
        match topic_choice:
            case "Sports":
                broker.queues["Sports"].put(f"{topic_choice} {sports_counter}")
                sports_counter += 1
            case "News":
                broker.queues["News"].put(f"{topic_choice} {news_counter}")
                news_counter += 1
            # case "Tech":
            #     broker.queues["Tech"].put(f"{topic_choice} {tech_counter}")
            #     tech_counter += 1
        sleep(4)


if __name__ == "__main__":
    broker = Broker()
    publisher = Thread(target=publisher_worker)

    publisher.start()
    broker.start()
