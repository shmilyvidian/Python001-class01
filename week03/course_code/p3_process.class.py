import os
from multiprocessing import Process
import time


class NewProcess(Process):
    def __init__(self, num):
        self.num = num
        super().__init__()

    def run(self):
        while True:
            print(f'我是进程 {self.num}, 我的pid是 {os.getpid()}')
            time.sleep(1)


for i in range(2):
    p = NewProcess(i)
    p.start()
