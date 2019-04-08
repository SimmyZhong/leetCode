"""
https://leetcode-cn.com/problems/basic-calculator/
实现一个基本的计算器来计算一个简单的字符串表达式的值。

字符串表达式可以包含左括号 ( ，右括号 )，加号 + ，减号 -，非负整数和空格  。

示例 1:

输入: "1 + 1"
输出: 2
示例 2:

输入: " 2-1 + 2 "
输出: 3
示例 3:

输入: "(1+(4+5+2)-3)+(6+8)"
输出: 23
说明：

你可以假设所给定的表达式都是有效的。
请不要使用内置的库函数 eval。
"""
import operator


class Solution2:
    def calculate(self, s: str) -> int:
        stack = list()
        Operator = {"+": add, "-": mimus, "*": plus, "/": div}
        num = 0
        for each in s[::-1]:
            # print(stack)
            if each == ")":
                while stack:
                    oper = stack.pop()
                    if oper not in Operator:
                        break
                    item = stack.pop()
                    num = Operator[oper](item, num)
            elif each in Operator:
                stack.append(num)
                stack.append(each)
                num = 0
            elif each == "(":
                stack.append(each)
            elif not each == " ":
                num = num * 10 + int(each)
        if not stack:
            return num
        print(stack, num)
        while stack:
            oper = stack.pop()
            item = stack.pop()
            num = Operator[oper](item, num)
        return num


def add(x, y):
    return x + y

def mimus(x, y):
    return x - y

def plus(x, y):
    return x * y

def div(x, y):
     return x / y


test_case = [ "(1+(4+5+2)-3)+(6+8)", "4-5+2", "1-2"]
for each in test_case:
    print(Solution().calculate(each))