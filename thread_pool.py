from multiprocessing.pool import ThreadPool
from time import sleep
import random

def worker(sleep_time: int, name: str) -> None:
    for i in range(10):
        print(f"{name} (sleep {sleep_time}s): {i}")
        sleep(sleep_time)
    print(f"{name} encerrada.")

n = 3
random_sleep_times = [(1, f"Thread-1"), (2, f"Thread-2"), (3, f"Thread-3")]

with ThreadPool(processes=n) as p:
    p.starmap(worker, random_sleep_times)
