class Node(object):
    # python类各方法实现

    def __new__(cls, *args, **kw):
        # 单例
        if not hasattr(cls, "_instance"):
            cls._instance = super(Node, cls).__new__(cls)
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


def main():
    n1 = Node('abcdef')
    n2 = Node('ABCDEF')
    assert(n1 is n2)
    assert(n1[0] == "A")
    assert(next(n1) == "A")
    a = "".join([each for each in n1])
    assert(a == "BCDEF")
    assert(len(n1) == 6)

if __name__ == "__main__":
    main()
