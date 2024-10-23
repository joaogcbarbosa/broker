import os
from time import sleep

pid = os.fork()

if pid < 0:
    print("fork failed")
elif pid == 0:
    for i in range(1, 11):
        print(i)
        if i == 10:
            print(i/0)
        sleep(0.5)
else:
    child_pid, child_exit_code = os.wait()
    print(
        "processo filho, de pid {}, terminou a execução com código de saída {}, continuando processo pai, de pid {}".format(
            child_pid, child_exit_code, os.getpid()
        )
    )
    for i in range(11, 21):
        print(i)
        sleep(0.5)
