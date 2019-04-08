"""
https://leetcode-cn.com/problems/sqrtx/https://leetcode-cn.com/problems/sqrtx/
实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:

输入: 4
输出: 2
示例 2:

输入: 8
输出: 2
说明: 8 的平方根是 2.82842..., 
     由于返回类型是整数，小数部分将被舍去。
"""

class Solution:
    # 牛顿迭代法
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 1:
            return x
        r = x
        while r > x / r:
            r = (r + x / r) // 2
        return int(r)


class Solution2:
    # 拓展：如何求解一元多次方程的解

    def mySqrt(self, x):
        left, right = 0, x
        while left + 1 < right:
            mid = (left + right) // 2
            if mid * mid < x:
                left = mid
            elif mid * mid > x:
                right = mid
            else:
                return mid
        return left

    def fx(self, x):
        return x*x*x + 7 * x -12
    def ffx(self, x):
        return 3 * x * x + 7

    def mySqrt2(self, x):
        r = x
        while abs(self.fx(r)) > 0.001:
            r = r - self.fx(r) / self.ffx(r)
        return r
