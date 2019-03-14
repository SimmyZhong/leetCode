"""
https://leetcode-cn.com/problems/min-stack/
设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) -- 将元素 x 推入栈中。
pop() -- 删除栈顶的元素。
top() -- 获取栈顶元素。
getMin() -- 检索栈中的最小元素。
示例:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.
"""


class ListNode:
    """
    链表
    """
    def __init__(self, v):
        self.val = v
        self.next = None
        self.minValue = v


class MinStack(object):

    def __init__(self):
        self.items = None

    def push(self, val):
        """
        压入栈
        """
        newInterval = ListNode(val)
        if self.items:
            newInterval.next = self.items
            if self.items.minValue < val:
                newInterval.minValue = self.items.minValue
        self.items = newInterval

    def pop(self):
        """
        删除栈顶元素
        """
        if self.items:
            self.items = self.items.next

    def top(self):
        """
        获取栈顶元素
        """
        return self.items.val if self.items else None

    def getMin(self):
        if not self.items:
            return None
        return self.items.minValue

def TestCase():
    funcList = ["push", "push", "push", "getMin", "pop", "top", "getMin", "push", "top", "getMin"]
    argsList = [[-2], [0], [-3], [], [], [], [], [-10], [], []]
    item = MinStack()
    results = []
    while funcList:
        func = funcList.pop(0)
        args = argsList.pop(0)
        arg = True if args else False
        if arg:
            result = (getattr(item, func))(args[0])
        else:
            result = (getattr(item, func))()
        results.append(result)
    assert([None, None, None, -3, None, 0, -2, None, -10, -10] == results)
    print("Test OK")


if __name__ == "__main__":
    TestCase()
