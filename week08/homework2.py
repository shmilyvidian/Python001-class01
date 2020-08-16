# 自定义一个 python 函数，实现 map() 函数的功能。
class MyMap:
    def __init__(self, func, *args):
        self.iterators = args
        self.func = func

    def __iter__(self):
        return self.generator()

    def generator(self):
        iterators, func = self.iterators, self.func
        try:
            i = 0
            while 1:
                yield func(*[j[i] for j in iterators])
                i += 1
        except IndexError:
            print(IndexError)