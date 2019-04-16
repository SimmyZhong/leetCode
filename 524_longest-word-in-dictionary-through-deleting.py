"""
https://leetcode-cn.com/problems/longest-word-in-dictionary-through-deleting/
给定一个字符串和一个字符串字典，找到字典里面最长的字符串，该字符串可以通过删除给定字符串的某些字符来得到。如果答案不止一个，返回长度最长且字典顺序最小的字符串。如果答案不存在，则返回空字符串。

示例 1:

输入:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

输出: 
"apple"
示例 2:

输入:
s = "abpcplea", d = ["a","b","c"]

输出: 
"a"
说明:

所有输入的字符串只包含小写字母。
字典的大小不会超过 1000。
所有输入的字符串长度不会超过 1000。
"""
class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        d = sorted(d, key=lambda each: len(each), reverse=True)
        result = ""
        for each in d:
            if len(each) < len(result):
                break
            if self.filterList(s, each):
                if len(each) > len(result):
                    result = each
                else:
                    if result[0] < each[0]:
                        continue
                    result = each
        return result
    
    def filterList(self, s, word):
        if len(word) > len(s):
            return False
        for each in word:
            if s.find(each) == -1:
                return False
            s = s[s.find(each)+1:]
        return True