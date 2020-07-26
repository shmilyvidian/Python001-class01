from threading import Event, Thread
import time

# 先生成一个event对象
e = Event()


def light():
    print('红灯正亮着')
    time.sleep(3)
    e.set()  # 发信号
    print('绿灯亮了')


def car(name):
    print('%s正在等红灯' % name)
    e.wait()  # 等待信号
    print('%s加油门飙车了' % name)


t = Thread(target=light)
t.start()

for i in range(2):
    t = Thread(target=car, args=('伞兵%s' % i,))
    t.start()
