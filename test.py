class Node(object):

	def __init__(self, val):
		self.val = val

	def __getitem__(self, k):
		return getattr(self, k)

a = Node('ac')
print(a["val"])
print(a.val)