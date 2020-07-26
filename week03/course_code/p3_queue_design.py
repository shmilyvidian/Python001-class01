import queue
import time
import threading
import random
lock = threading.Lock()


class Producer(threading.Thread):
    def __init__(self, q, conn, name):
        super(Producer, self).__init__()
        self.q = q
        self.conn = conn
        self.name = name
        print(f'=Producer {self.name} is start==')

    def run(self):
        while 1:
            global lock
            self.conn.acquire()
            if self.q.full():
                with lock:
                    print('queue is full')
                self.conn.wait()
            else:
                value = random.randint(0, 10)
                with lock:
                    print(f'{self.name} put value {self.name} {value} in queue')
                self.q.put((f'{self.name} : {value}'))
                self.conn.notify()
                time.sleep(1)
            self.conn.release()


class Consumer(threading.Thread):
    def __init__(self, q, conn, name):
        super(Consumer, self).__init__()
        self.q = q
        self.conn = conn
        self.name = name
        print(f'=Consumer {self.name} is start==')

    def run(self):
        while 1:
            global lock
            self.conn.acquire()
            if self.q.empty():
                with lock:
                    print('queue is empty')
                self.conn.wait()
            else:
                value = self.q.get()
                with lock:
                    print(f'{self.name} get value {value} in queue')
                self.conn.notify()
                time.sleep(1)
            self.conn.release()


if __name__ == "__main__":
    q = queue.Queue(10)
    c = threading.Condition()

    p1 = Producer(q, c, 'p1')
    p1.start()

    p2 = Producer(q, c, 'p2')
    p2.start()

    c1 = Consumer(q, c, 'c1')
    c1.start()
