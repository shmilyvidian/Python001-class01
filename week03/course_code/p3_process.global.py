from multiprocessing import Process
num = 100


def run():
    print('子进程开始')
    global num
    num += 1
    print(f'子进程num {num}')
    print('子进程结束')


if __name__ == "__main__":
    print('父进程开始')
    p = Process(target=run)
    p.start()
    p.join()
    print('父进程结束')
    print(f'父进程num {num}')

# 子进程中修改全局变量对父进程中的全局变量无影响
