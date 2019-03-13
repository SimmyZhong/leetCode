import random


class ListNode:
    """
    链表
    """
    def __init__(self, v):
        self.val = v
        self.next = None

    @staticmethod
    def getListNode(NodeLen):
        """
        获取长度为NodeLen的随机链表
        """
        TestListNode, ListNodeLen = ListNode(0), 0
        curNode = TestListNode
        while ListNodeLen < NodeLen:
            ListNodeLen += 1
            curNode.next = ListNode(random.choice(range(-10000, 10000)))
            curNode = curNode.next
        return TestListNode.next


def listNodeToList(headNode):
    """
    链表转为数组
    """
    result = []
    while headNode:
        result.append(headNode.val)
        headNode = headNode.next
    return result
