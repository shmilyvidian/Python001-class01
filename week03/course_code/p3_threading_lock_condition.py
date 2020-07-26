import threading


def f():
    ret = False
    r = input('>>>')
    if r == 'yes':
        ret = True
    return ret


def func(conn, i):
    conn.acquire()
    conn.wait_for(f)
    print(i+100)
    conn.release()


if __name__ == "__main__":
    c = threading.Condition()
    for i in range(5):
        t = threading.Thread(target=func, args=(c, i, ))
        t.start()
