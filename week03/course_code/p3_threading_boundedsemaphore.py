import threading
import time


def run(conn, i):
    conn.acquire()
    print(f'=={i}==')
    time.sleep(2)
    conn.release()


if __name__ == "__main__":
    conn = threading.BoundedSemaphore(5)
    for i in range(10):
        t = threading.Thread(target=run, args=(conn, i))
        t.start()
