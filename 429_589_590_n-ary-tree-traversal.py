"""
层序遍历：https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal/
前序遍历：https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/
后序遍历：https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/
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

返回其前序遍历:
[1,3,5,6,2,4]

返回其后序遍历:
[5,6,3,2,4,1]

说明:

树的深度不会超过 1000。
树的节点总数不会超过 5000。
"""


# Definition for a Node.
class Node:
	"""n叉树"""
	def __init__(self, val, children):
		self.val = val
		self.children = children


class Solution:
	def levelOrder(self, root):
		"""层级遍历"""
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

	def preOrderIter(self, root):
		"""前序遍历迭代法"""
		if not root:
			return []
		result, stack = [], [root]
		while stack:
			root = stack.pop()
			result.append(root.val)
			if root.children:
				for idx in range(len(root.children)-1, -1, -1):
					stack.append(root.children[idx])
		return result

	def preOrderRecursion(self, root):
		"""前序遍历递归法"""
		if not root:
			return []
		result = [root.val]
		if root.children:
			for each in root.children:
				result.extend(self.preorder(each))
		return result

	def postOrderInter(self, root):
		"""后序遍历迭代法"""
		if not root:
			return []
		result, stack = [], [root]
		while stack:
			root = stack.pop()
			result.insert(0, root.val)
			if root.children:
				for each in root.children:
					stack.append(each)
		return result

	def postOrderRecursion(self, root):
		"""后序遍历递归法"""
		if not root:
            return []
        result, stack = [], [root]
        while stack:
            root = stack.pop()
            result.insert(0, root.val)
            if root.children:
                for each in root.children:
                    stack.append(each)
        return result