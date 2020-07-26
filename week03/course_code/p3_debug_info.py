import multiprocessing
import os


def debug_info(title):
    print('-'*20)
    print(title)
    print(f'父进程 {os.getppid()}')
    print(f'当前进程 {os.getpid()}')
    print('-'*20)


def f(name):
    debug_info('f')
    print(f'hello {name}')


if __name__ == "__main__":
    debug_info('main')
    p = multiprocessing.Process(target=f, args=('bob',), name='shmilyvidian')
    p.start()

    for p in multiprocessing.active_children():
        print(f'子进程ID {p.pid} 子进程名称 {p.name}')
    print('进程结束')
    print(f'CPU核心数量： {multiprocessing.cpu_count()}')
    p.join()
    print('end')

