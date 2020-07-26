import threading

class MyThread(threading.Thread):
    def __init__(self, num):
        super().__init__()
        self.num = num
    
    def run(self):
        print(f'name {self.name}')


def f(name):
    print(f'name {name}')


if __name__ == "__main__":
    # t1 = threading.Thread(target=f, args=('t1',))
    # t2 = threading.Thread(target=f, args=('t2',))
    # t1.start()
    # t2.start()
    # t1.join()
    # t2.join()
    t1 = MyThread('t1')
    t2 = MyThread('t2')
    t1.start()
    t2.start()
    print('main')
