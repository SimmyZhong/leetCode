"""
https://leetcode-cn.com/problems/insertion-sort-list/
插入排序算法：

插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
重复直到所有输入数据插入完为止。
 

示例 1：

输入: 4->2->1->3
输出: 1->2->3->4
示例 2：

输入: -1->5->3->4->0
输出: -1->0->3->4->5
"""

import random

from dataStructure.listNode import ListNode, listNodeToList


class Solution:
    """
    链表插入排序实现
    """
    def sortList(self, head):
        """
        插入排序
        """
        if not head:
            return head
        result = ListNode(head.val)
        while head.next:
            result = self.__InsertNode(ListNode(head.next.val), 0, result)
            head = head.next
        return result

    def __InsertNode(self, headNode, FormerNode, ListNode):
        """
        节点插入有序链表
        """
        headNode.next = None
        if headNode.val > ListNode.val:
            if ListNode.next:
                self.__InsertNode(headNode, ListNode, ListNode.next)
            else:
                ListNode.next = headNode
            return ListNode
        else:
            headNode.next = ListNode
            if FormerNode:
                FormerNode.next = headNode
            return headNode

def testCase():
    """
    Test case
    """
    for each in [0, 1, 15, 30, 60]:
        testListNode = ListNode.getListNode(each)
        oriList = listNodeToList(testListNode)
        sortList = listNodeToList(Solution().sortList(testListNode))
        # 验证结果
        assert(sorted(oriList) == sortList)
    print("Test OK")


if __name__ == "__main__":
    testCase()