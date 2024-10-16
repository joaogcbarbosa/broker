from queue import Queue
from threading import Thread
from time import sleep

from models.broker import Publisher, Subscriber
from app.utils.worker import worker


def main():
    sports_publisher = Publisher(id=1, topic="Sports")
    news_publisher = Publisher(id=2, topic="News")
    tech_publisher = Publisher(id=3, topic="Technology")
    
    broker = Queue()

    subscriber_01 = Subscriber(id=1, name="João", subscriptions=[tech_publisher, sports_publisher])
    subscriber_02 = Subscriber(id=2, name="Gustavo", subscriptions=[tech_publisher])
    subscriber_03 = Subscriber(id=3, name="Paulo", subscriptions=None)
    subscriber_04 = Subscriber(id=4, name="Bernardo", subscriptions=[sports_publisher, news_publisher, tech_publisher])


    message_counter = 1
    while True:
        sports_thread = Thread(
            target=worker(topic=sports_publisher.topic, message_number=message_counter, broker_queue=broker)
        )
        news_thread = Thread(
            target=worker(topic=news_publisher.topic, message_number=message_counter, broker_queue=broker)
        )
        tech_thread = Thread(
            target=worker(topic=tech_publisher.topic, message_number=message_counter, broker_queue=broker)
        )
        sports_thread.start()
        news_thread.start()
        tech_thread.start()
        print(broker.queue)
        sleep(3)
        message_counter += 1


if __name__ == "__main__":
    main()
