"""
https://leetcode-cn.com/problems/sort-list/
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

示例 1:

输入: 4->2->1->3
输出: 1->2->3->4

示例 2:

输入: -1->5->3->4->0
输出: -1->0->3->4->5
"""

import random

from dataStructure.listNode import ListNode, listNodeToList


class Solution:
    """
    链表归并排序实现
    """
    def sortList(self, head):
        """
        归并排序
        """
        if not head or not head.next:
            return head
        n1, n2 = self.__sepaNode(head)
        return self.__mergeNode(self.sortList(n1), self.sortList(n2))

    def __sepaNode(self, headNode):
        """
        中位拆分链表
        """
        p1, p2 = headNode, headNode
        pre = None
        while (p1 and p1.next):
            p1 = p1.next.next
            pre = p2
            p2 = p2.next
        pre.next = None
        return headNode, p2

    def __mergeNode(self, n1, n2):
        """
        合并链表
        """
        result = ListNode(0)
        b = result
        while (n1 and n2):
            if n1.val < n2.val:
                b.next = b = n1
                n1 = n1.next
            else:
                b.next = b = n2
                n2 = n2.next
        b.next = n1 if n1 else n2
        return result.next


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
    



