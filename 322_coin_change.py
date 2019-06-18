"""
https://leetcode-cn.com/problems/coin-change/
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

示例 1:

输入: coins = [1, 2, 5], amount = 11
输出: 3 
解释: 11 = 5 + 5 + 1
示例 2:

输入: coins = [2], amount = 3
输出: -1
说明:
你可以认为每种硬币的数量是无限的。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/coin-change
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

import sys


class Solution:
	def change(self, nums,target):
		# 动态规划 f(n) = min([f(n-i)+1 for i in nums])
		resp = [0] * (target+1)
		for i in range(1, target+1):
			cur = sys.maxsize
			for each in nums:
				if i - each >= 0:
					cur = min(cur, resp[i-each]+1)
			resp[i] = cur
		return resp[target] if resp[target] != sys.maxsize else -1

	def change_dfs(self, nums, target):
		# 深度优先遍历，容易超时
		resp = sys.maxsize
		def helper(start, temp):
			nonlocal resp
			if sum(temp) == target:
				if len(temp) < resp:
					resp = len(temp)
				return
			elif sum(temp) > target:
				return
			for i in range(start, len(nums)):
				helper(i, temp+[nums[i]])
		helper(0, [])
		return resp if resp != sys.maxsize else -1


def main():
	print(Solution().change([1, 2, 5], 11))
	print(Solution().change_dfs([1, 2, 5], 11))


if __name__ == '__main__':
	main()