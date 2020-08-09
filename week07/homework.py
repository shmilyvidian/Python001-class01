from abc import ABCMeta, abstractmethod

# 定义一个抽象基类


class Animal(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, mold, body, character, isViolent):
        self.mold = mold
        self.body = body
        self.character = character
        if self.body >= '中等' and self.mold == '食肉类型' and self.character == '性格凶猛':
            self.isViolent = True
        else:
            self.isViolent = False


class Cat(Animal):
    def __init__(self, name, mold, size, character):
        self.name = name
        self.mold = mold
        self.size = size
        self.character = character
        super().__init__(self.mold, self.size, self.character, '')


def getattr(cls, name):
    for key in cls.animals.keys():
        if name in key:
            print(f"{name}已经存在")
            break
        else:
            print(f"没有{name}这个动物")


class Zoo(object):
    def __init__(self, name):
        self.name = name
        self.animals = {}

    def add_animal(self, cls):
        temp_id = id(cls)
        key_animal = str(type(cls))
        if self.animals.get(key_animal) == None:
            self.animals[key_animal] = [temp_id]
        elif (self.animals.get(key_animal) != None) and (temp_id not in self.animals[key_animal]):
            self.animals[key_animal].append(temp_id)
        else:
            print(f"{cls.name}已经存在")


if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    print(z, 'z')
    # # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    # # 增加一只猫到动物园
    z.add_animal(cat1)
    # # 动物园是否有猫这种动物
    have_cat = getattr(z, 'Cat')
