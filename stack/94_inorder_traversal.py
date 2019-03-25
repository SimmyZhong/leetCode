"""
https://leetcode-cn.com/problems/binary-tree-inorder-traversal/
给定一个二叉树，返回它的中序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
"""


class Solution:

	def inorderTraversal(rootNode):
		"""
		递归法
		"""
		result = []
		if not rootNode:
			return result
		elif rootNode.left:
			result.extend(self.inorderTraversal(rootNode.left))
		result.append(rootNode.val)
		if rootNode.right:
			result.extend(self.inorderTraversal(rootNode.right))
		return result

	def inorderTraversal_2(rootNode):
		"""
		栈迭代法
		"""
        result = []
        stack = []  # 利用python的list作为栈用
        if not rootNode:
            return result
        while rootNode or stack:
            if rootNode:
                stack.append(rootNode)
                rootNode = rootNode.left
            else:
                rootNode = stack.pop()
                result.append(rootNode.val)
                rootNode = rootNode.right
        return result

