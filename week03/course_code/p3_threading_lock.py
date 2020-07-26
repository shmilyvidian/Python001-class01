import threading
import time

num = 0

mlock = threading.RLock()


def count():

    global num
    time.sleep(1)
    if mlock.acquire():
        num += 1
        mlock.acquire()

        print(f'num {num}')
        mlock.release()
    mlock.release()


if __name__ == "__main__":
    for _ in range(10):
        t = threading.Thread(target=count)
        t.start()
