from multiprocessing import Process, Value, Array


def f(n, a):
    n.value = 3.1415927178
    for i in a:
        a[i] *= 2


if __name__ == "__main__":
    num = Value('d', 0.0)
    arr = Array('i', range(10))
    p = Process(target=f, args=(num, arr))
    p.start()
    p.join()
    print(f'num {num.value} arr {arr[:]}')