"""
https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal/
给定一个 N 叉树，返回其节点值的层序遍历。 (即从左到右，逐层遍历)。

例如，给定一个 3叉树 :
    1
  / | \
  3 2 4
 /\
 5 6

返回其层序遍历:

[
     [1],
     [3,2,4],
     [5,6]
]
 

说明:

树的深度不会超过 1000。
树的节点总数不会超过 5000。
"""


# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        queue, result = [root], []
        while queue:
            new_queue, val_list = [], []
            for each in queue:
                val_list.append(each.val)
                if each.children:
                    new_queue.extend(each.children)
            queue = new_queue
            result.append(val_list)
        return result