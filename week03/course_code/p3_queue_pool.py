from multiprocessing.dummy import Pool as ThreadPool
import requests
from concurrent.futures import ThreadPoolExecutor
import time

urls = [
    'http://www.baidu.com',
    'http://www.sina.com.cn',
    'http://www.qq.com',
    'http://www.taobao.com',
]


def func(args):
    print(f'call func {args}')


if __name__ == "__main__":
    # pool = ThreadPool(4)
    # results = pool.map(requests.get, urls)
    # pool.close()
    # pool.join()

    # for i in results:
    #     print(i.url)
    seed = ['a', 'b', 'c', 'd']
    with ThreadPoolExecutor(3) as extector:
        extector.submit(func, seed)

    time.sleep(1)

    with ThreadPoolExecutor(2) as extector1:
        extector1.map(func, seed)

    time.sleep(1)

    with ThreadPoolExecutor(max_workers=1) as extector3:
        future = extector3.submit(pow, 2, 3)
        print(future.result())

