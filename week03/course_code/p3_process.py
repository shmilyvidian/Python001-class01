from multiprocessing import Process


def f(name, **k):
    age = k['age']
    print(f'name {name} age {age}')


if __name__ == "__main__":
    p = Process(target=f, args=('children',), kwargs={'age': 1})
    p.start()
    p.join()  # 父进程等待子进程结束才关闭
    print('-----')
