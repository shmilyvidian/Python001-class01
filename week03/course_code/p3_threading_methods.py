import threading
import time


def start():
    time.sleep(5)


if __name__ == "__main__":
    t = threading.Thread(target=start, name='shmilyvidian')
    t.start()

    name = t.getName()
    alive_1 = t.is_alive()
    print(f'name {name}, alive_1 {alive_1}')
    t.join()
    alive_2 = t.is_alive()
    print(f'name {name}, alive_2 {alive_2}')
