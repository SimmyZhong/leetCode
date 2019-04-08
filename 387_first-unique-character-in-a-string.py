"""
https://leetcode-cn.com/problems/first-unique-character-in-a-string/
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

案例:

s = "leetcode"
返回 0.

s = "loveleetcode",
返回 2.
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        choice = list()
        for each in s:
        	choice[ord(each)] += 1
        for each in s:
        	if choice[ord(each)] == 1:
        		return ord(each)
        return -1
