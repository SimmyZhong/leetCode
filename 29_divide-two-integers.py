"""
https://leetcode-cn.com/problems/divide-two-integers/
给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数 dividend 除以除数 divisor 得到的商。

示例 1:

输入: dividend = 10, divisor = 3
输出: 3
示例 2:

输入: dividend = 7, divisor = -3
输出: -2
说明:

被除数和除数均为 32 位有符号整数。
除数不为 0。
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。本题中，如果除法结果溢出，则返回 231 − 1。
"""


class Solution:
	def divide(self, dividend, divisor):
		result = 0
		flag = (divisor > 0) == (dividend > 0)
		dividend, divisor = abs(dividend), abs(divisor)
		while True:
			if dividend < divisor:
				break
			for i in range(31, -1, -1):
				value = 2**i
				if value * divisor <= dividend:
					result += value
					dividend = dividend - value * divisor
					break
		result = result if flag else -result
		if result < -2147483648:
			return -2147483648
		elif result > 2147483647:
			return 2147483647
		else:
			return result