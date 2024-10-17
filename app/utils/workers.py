from queue import Queue
from time import sleep

publications_list = []

def sports_publisher(broker: Queue) -> None:
    while True:
        message = broker.get()
        publications_list.append(message)
        broker.task_done()


def sports_subscriber(subscriber: str) -> None:
    while True:
        for p in publications_list:
            if "Sports" in p:
                print(f"{subscriber} recebeu {p}")
        sleep(3)

# def news_worker():
#     message_list = []
#     while True:
#         item = broker.get()
#         message_list.append(item)
#         print(message_list)
#         broker.task_done()


# def technology_worker():
#     message_list = []
#     while True:
#         item = broker.get()
#         message_list.append(item)
#         print(message_list)
#         broker.task_done()