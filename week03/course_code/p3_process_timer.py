import threading


def run(name, **k):
    print(f"age {k['age']}")
    print('我是一秒后打印的hello', name)


if __name__ == "__main__":
    t = threading.Timer(1, run, args=('shmilyvidian',), kwargs={'age': 2})
    t.start()
