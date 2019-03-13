"""
https://leetcode-cn.com/problems/largest-number/
给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。

示例 1:

输入: [10,2]
输出: 210
示例 2:

输入: [3,30,34,5,9]
输出: 9534330
说明: 输出结果可能非常大，所以你需要返回一个字符串而不是整数。
"""


class Solution:
	
	def largestNumber(self, numList):
		sortList = self.__mergeSort(numList)
		result = ''.join([str(each) for each in sortList])
		# 防止"00"这种情况存在
		return "0" if result.startswith('0') else result

	def __mergeSort(self, numList):
		"""
		采用归并法排序
		"""
		if len(numList) <= 1:
			return numList
		middle = len(numList) // 2
		leftList, rightList = numList[:middle], numList[middle:]
		return self.mergeList(self.__mergeSort(leftList), self.__mergeSort(rightList))

	def mergeList(self, leftList, rightList):
		"""
		合并列表
		"""
		result = []
		while (leftList and rightList):
			if self.__compare(leftList[0], rightList[0]):
				result.append(rightList.pop(0))
			else:
				result.append(leftList.pop(0))
		result.extend(leftList) if leftList else result.extend(rightList)
		return result

	def __compare(self, num1, num2):
		"""
		两数对比，按最高位对比
		"""
		n1, n2 = int(''.join([str(num1), str(num2)])), int(''.join([str(num2), str(num1)]))
		return True if n1 < n2 else False

def testCase():
	assert("0" == Solution().largestNumber([0, 0]))
	assert("34312121" == Solution().largestNumber([12, 121, 343]))
	assert("856574545343321211" == Solution().largestNumber([5657, 121, 343, 32, 1, 8, 4545]))
	print("Test OK")


if __name__ == '__main__':
	testCase()

