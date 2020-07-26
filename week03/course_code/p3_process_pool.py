import multiprocessing as mp
import os
import time
import random


def run(name):
    print(f'子进程开始进程ID {os.getpid()} 名称为 {name}')
    startTime = time.time()
    time.sleep(random.choice([1, 2, 3, 4]))
    endTime = time.time()
    print(f'子进程结束 耗时为{endTime - startTime}')


if __name__ == "__main__":
    print('父进程开始')
    p = mp.Pool(mp.cpu_count())
    for i in range(20):
        p.apply_asyn(run, args=(i,))
    p.close()
    p.join()
    p.terminate()
    print('父进程结束')