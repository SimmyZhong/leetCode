"""
实现一个二叉搜索树迭代器。你将使用二叉搜索树的根节点初始化迭代器。

调用 next() 将返回二叉搜索树中的下一个最小的数。

示例：

   7
  / \
 3  15
    / \
   9  20

BSTIterator iterator = new BSTIterator(root);
iterator.next();    // 返回 3
iterator.next();    // 返回 7
iterator.hasNext(); // 返回 true
iterator.next();    // 返回 9
iterator.hasNext(); // 返回 true
iterator.next();    // 返回 15
iterator.hasNext(); // 返回 true
iterator.next();    // 返回 20
iterator.hasNext(); // 返回 false
 
提示：
next() 和 hasNext() 操作的时间复杂度是 O(1)，并使用 O(h) 内存，其中 h 是树的高度。
你可以假设 next() 调用总是有效的，也就是说，当调用 next() 时，BST 中至少存在一个下一个最小的数。
"""


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root = root
        self.__item = self.__inorderTraversal(root)
        
    def next(self) -> int:
        """
        @return the next smallest number
        """
        item = self.root
        while item.left:
            item = item.left
        if item.right:
            item = item.right
        else item = None

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return True if self.__item else False
    
    def __inorderTraversal(self, rootNode):
        """
        参考94题二叉搜索树的中序遍历得到排好序的list
        """
        result = []
        stack = []
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