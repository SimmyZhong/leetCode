from functools import wraps


class Node(object):
    # python类各方法实现

    def __new__(cls, *args, **kw):
        # 单例
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, val):
        # 初始化
        self.__val = val
        self.index = 0

    def __next__(self):
        # 迭代器
        try:
            result =  self.__val[self.index]
        except IndexError:
            raise StopIteration
        else:
            self.index += 1
            return result

    def __iter__(self):
        # 可迭代对象
        return self

    def __getitem__(self, index):
        # 切片
        return self.__val[index]

    def __len__(self):
        # 长度
        return len(self.__val)

    def __str__(self):
        # 格式化
        return self.__val

    def __getattr__(self, key):
        print("__getattr__ function is calling.")
        return super().__getattribute__(key)

    def __getattribute__(self, key):
        if key == "test":
            print("__getattribute__ function is calling and then raise AttributeError.")
            raise AttributeError
        return super().__getattribute__(key)

    def __setattr__(self, key, value):
        if key == "test":
            print("attr is set.")
        return super().__setattr__(key, value)

    # with的用法
    # 紧跟with后面的语句被求值后，返回对象的__enter__方法被调用，这个方法的返回值将被赋值给as后面的变量,
    # 当with后面的代码块全部被执行完之后，将调用前面返回对象的__exit__方法。 
    def __enter__(self):
        print("---in entering---")
        return self

    def __exit__(self, exc_type, exc_value, tracback):
        print("---in exit---")


def testDecorator(text):
    print("decorator params: ", text)
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kw):
            print("---in test decorator---")
            return func(*args, **kw)
        return inner
    return wrapper


@testDecorator('aaaa')
def main():
    n1 = Node('abcdef')
    n2 = Node('ABCDEF')
    assert(n1 is n2)
    print(n1[:34])
    assert(next(n1) == "A")
    a = "".join([each for each in n1])
    print(a)
    assert(a == "BCDEF")
    assert(len(n1) == 6)
    n1.test = "test: getattr"
    print(n1.test)
    print(hasattr(n1, "tt"))
    with n1 as n:
        print(n)

if __name__ == "__main__":
    main()
