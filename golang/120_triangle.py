"""
https://leetcode-cn.com/problems/triangle/
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。

例如，给定三角形：

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

说明：

如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。
"""


class Solution:
    def minimumTotal(self, triangle):
        """求最小值"""
        min_len = triangle[-1]
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                min_len[j] = triangle[i][j] + min(min_len[j+1], min_len[j])
            min_len.pop()
        return min_len[0]

    def maxiumTotal(self, triangle):
        """求最大值"""
        max_len = triangle[-1]
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                max_len[j] = max(max_len[j], max_len[j+1]) + triangle[i][j]
        return max(max_len)