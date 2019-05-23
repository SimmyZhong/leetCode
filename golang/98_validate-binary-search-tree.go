/*
https://leetcode-cn.com/problems/validate-binary-search-tree/
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
示例 1:

输入:
	2
   / \
  1   3
输出: true
示例 2:

输入:
	5
   / \
  1   4
	 / \
	3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
	 根节点的值为 5 ，但是其右子节点值为 4 。

*/


package main

import (
	"fmt"
)

type TreeNode struct {
	Val int
	Left *TreeNode
	Right *TreeNode
}

func isValidBST(root *TreeNode) bool {
	// 定义最小整数
	var curVal = ^int(^uint(0)>>1)
	var stack []*TreeNode
	for root != nil || len(stack) != 0 {
		if root != nil {
			// 入栈
			stack = append(stack, root)
			root = root.Left
		} else if len(stack) != 0 {
			// 出栈
			root, stack = stack[len(stack)-1],  stack[:len(stack)-1]
			if curVal < root.Val {
				curVal = root.Val
			} else {
				return false
			}
			root = root.Right
		}
	}
	return true
}

// 方法2
func isValidBST2(root *TreeNode) bool {
	return isValid(root, ^int(^uint(0)>>1), int(^uint(0)>>1))
}

func isValid(node *TreeNode, minVal, maxVal int) bool {
	if node == nil {
		return true
	}
	return node.Val < maxVal &&node.Val > minVal && isValid(node.Left, minVal, node.Val) && isValid(node.Right, node.Val, maxVal)
	 
}


	