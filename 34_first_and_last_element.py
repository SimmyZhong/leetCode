"""
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]
"""


class Solution:
	def searchRange(self, nums, target):
        # 通过二分查找定位到元素索引，然后前后遍历得到最大最小值
		result = self.__twoDivide(nums, target)
		if result == -1:
			return [-1, -1]
		minKey, maxKey = result, result
		while True:
			if minKey <= 0 or nums[minKey - 1] != target:
				break
			minKey -= 1
		while True:
			if maxKey >= len(nums) - 1 or nums[maxKey + 1] != target:
				break
			maxKey += 1
		return [minKey, maxKey]		 

	def __twoDivide(self, nums, target):
        # 二分查找法
		if not nums:
			return -1
		left, right = 0, len(nums) - 1
		while left <= right:
			mid = (left + right) // 2
			val = nums[mid]
			if val == target:
				return mid
			elif val < target:
				left = mid + 1
			else:
				right = mid - 1
		return -1