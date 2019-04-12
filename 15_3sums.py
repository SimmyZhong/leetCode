"""
https://leetcode-cn.com/problems/3sum/submissions/
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
class Solution:
    def threeSum(self, nums):
        dict = {}
        pos=[]
        neg=[]
        for ele in nums:
            if ele not in dict:
                dict[ele] = 0
            dict[ele] += 1
            
        if 0 in dict and dict[0] > 2:
            result = [[0,0,0]]
        else:
            result = []
            
        for ele in dict:
            if ele>0:
                pos.append(ele)
            elif ele<0:
                neg.append(ele)
        
        for p in pos:
            for n in neg:
                target = -(p + n)
                if target in dict:
                    #两个相同的整数或者负数
                    if target in [p,n] and dict[target]>1:
                        result.append([p,n,target])
                    elif target < n or target > p or target == 0:
                        result.append([n, target, p])
                        
        return result

