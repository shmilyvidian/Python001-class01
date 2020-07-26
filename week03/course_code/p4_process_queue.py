from multiprocessing import Process, Queue


def f(q):
    q.put(['1', 'vidian', None])


if __name__ == "__main__":
    q = Queue()
    p = Process(target=f, args=(q,))
    p.start()
    print(q.get())
    p.join()
    print('end')
