from threading import Thread
from queue import Queue
from time import sleep
from random import randint
from utils.messager import sports_message
from utils.workers import sports_publisher, sports_subscriber

def main():
    broker = Queue()

    sports_publisher_thread = Thread(target=sports_publisher, args=(broker,), daemon=True)
    sports_subscriber_1_thread = Thread(target=sports_subscriber, args=("João",), daemon=True)
    sports_subscriber_2_thread = Thread(target=sports_subscriber, args=("Gustavo",), daemon=True)

    sports_publisher_thread.start()
    sports_subscriber_1_thread.start()
    sports_subscriber_2_thread.start()

    sports_counter = 1
    while True:
        broker.put(sports_message(sports_counter))
        sports_counter += 1
        sleep(4)


if __name__ == "__main__":
    main()