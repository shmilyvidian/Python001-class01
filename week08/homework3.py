# 实现一个 @timer 装饰器，记录函数的运行时间，注意需要考虑函数可能会接收不定长参数。
import datetime

def timer(func):

    def inner(*args, **kwargs):
        startTime = datetime.datetime.now()
        func(*args, **kwargs)
        endTime = datetime.datetime.now()
        print(f'函数运行了%{endTime-startTime}')

    return inner

@timer
def func(a,b,c=3):
    print(a+b+c)

func(3,2)
