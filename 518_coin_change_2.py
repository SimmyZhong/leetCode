"""
https://leetcode-cn.com/problems/coin-change-2/
给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。 

示例 1:

输入: amount = 5, coins = [1, 2, 5]
输出: 4
解释: 有四种方式可以凑成总金额:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
示例 2:

输入: amount = 3, coins = [2]
输出: 0
解释: 只用面额2的硬币不能凑成总金额3。
示例 3:

输入: amount = 10, coins = [10] 
输出: 1
 

注意:

你可以假设：

0 <= amount (总金额) <= 5000
1 <= coin (硬币面额) <= 5000
硬币种类不超过 500 种
结果符合 32 位符号整数

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/coin-change-2
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def change(self, nums, target):
        # 动态规划零钱组合
        resp = [1] + [0]*(target)
        for each in nums:
            for i in range(target+1):
                if i - each >= 0:
                    resp[i] += resp[i-each]

        return resp[target]

    def change_dfs(self, nums, target):
        # 深度优先遍历，但是容易超时
        resp = []
        def helper(start, temp):
            if sum(temp) == target:
                resp.append(temp)
            elif sum(temp) > target:
                return
            else:
                for i in range(start, len(nums)):
                    helper(i, temp + [nums[i]])
        helper(0, [])
        return len(resp)


def main():
    nums = [1, 2, 5]
    target = 11
    print(Solution().change_dfs(nums, target))
    print(Solution().change(nums, target))


if __name__ == '__main__':
    main()