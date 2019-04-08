"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true
"""


class Solution:

    def isValid(self, s):
        choice = {")": "(", "]": "[", "}": "{"}
        res = []
        s = list(s)
        while s:
            item = s.pop(0)
            if item in choice:
                if res and choice[item] == res[-1]:
                    res.pop(-1)
                else:
                    return False
            else:
                res.append(item)
        if res:
            return False
        return True


def testCase():
    testString = {
        "": True, "]": False, "{}": True, "[{}]": True,
        "[{)}]": False, "[(){{}}]": True, "](){}": False
    }
    for each in testString:
        assert(Solution().isValid(each) == testString[each])
    print("Test OK")


if __name__ == "__main__":
    testCase()
