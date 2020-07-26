import time
import os
from multiprocessing import Process


def run():
    print('子进程开启')
    time.sleep(2)
    print('子进程结束')


if __name__ == "__main__":
    print('父进程开启')
    p = Process(target=run)
    p.start()
    p.join()
    print('父进程结束')
