from multiprocessing import Process, Lock, Value
import time


def f(v, num, lock):
    lock.acquire()
    for _ in range(5):
        time.sleep(0.1)
        v.value += num
        print(v.value, end='|')
    lock.release()


if __name__ == "__main__":
    lock = Lock()
    v = Value('i', 0)
    # 元组
    p1 = Process(target=f, args=(v, 1, lock))
    p2 = Process(target=f, args=(v, 3, lock))
    p2.start()
    p1.start()
    p1.join()
    p2.join()