from queue import Queue


def worker(topic: str, message_number: int, broker_queue: Queue) -> None:
    if topic == "Sports":
        message = f"Sports News {message_number}"
        broker_queue.put(message)
        print(message)
    elif topic == "News":
        message = f"News News {message_number}"
        broker_queue.put(message)
        print(message)
    elif topic == "Technology":
        message = f"Technology News {message_number}"
        broker_queue.put(message)
        print(message)
    else:
        raise ValueError
