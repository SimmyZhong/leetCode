class TreeNode(object):
	"""树"""
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

	def PreOrderTraversal(self):
		"""前序遍历"""
		root, stack, result = self, [], []
		while True:
			if root:
				stack.append(root)
				result.append(root.val)
				root = root.left
			elif stack:
				root = stack.pop()
				root = root.right
			else:
				return result

	def InOrderTraveral(self):
		"""中序遍历"""
		root, stack, result = self, [], []
		while True:
			if root:
				stack.append(root)
				root = root.left
			elif stack:
				root = stack.pop()
				result.append(root.val)
				root = root.right
			else:
				return result

	def PostOrderTraveral(self):
		"""后序遍历"""
		stack, result = [self], []
		while stack:
			root = stack.pop()
			if root.left:
				stack.append(root.left)
			if root.right:
				stack.append(root.right)
			result.insert(0, root.val)
		return result

	def widthTraveral(self):
		"""层序遍历"""
		queue, result = [self], []
		while queue:
			root = queue.pop(0)
			result.append(root.val)
			if root.left:
				queue.append(root.left)
			if root.right:
				queue.append(root.right)
		return result

	def ThreeTraveral(self):
		"""三种遍历递归法"""
		result = dict(PreOrderTraversal=[], InOrderTraveral=[], PostOrderTraveral=[])
		result["PreOrderTraversal"].append(self.val)
		if self.left:
			for each in result:
				result[each].extend(self.left.ThreeTraveral()[each])
		result["InOrderTraveral"].append(self.val)
		if self.right:
			for each in result:
				result[each].extend(self.right.ThreeTraveral()[each])
		result["PostOrderTraveral"].append(self.val)
		return result

