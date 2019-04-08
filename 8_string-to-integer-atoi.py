class Solution:
    def myAtoi(self, str):
        str = str.lstrip()
        if not str:
            return 0
        nums = string.digits
        result = 0
        flag = False 
        if str[0] == "-":
            flag = True
        elif str[0] in nums:
            result = int(str[0])
        else:
            return 0

        for each in str[1:]:
            if each in nums:
                result = result * 10 + int(each)
            else:
                break
        if result > 2**31 - 1:
            return 2**31 - 1
        elif result < -2**31:
            return -2**31
        else:
            return result