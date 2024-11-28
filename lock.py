from multiprocessing.dummy import Pool as ThreadPool
from threading import Lock

buffer = []
buffer_lock = Lock()
to_append_lock = Lock()


def pusher(n: int) -> None:
    global buffer, to_append
    with buffer_lock:
        buffer.append(n)
        print(f"{n} adicionado")

    with to_append_lock:
        to_append.remove(n)
        print(f"Restantes na lista: {to_append}")


if __name__ == "__main__":
    to_append = list(range(100))
    with ThreadPool(4) as p:
        p.map(pusher, to_append)
    
    print(buffer)
    assert len(buffer) == 100
