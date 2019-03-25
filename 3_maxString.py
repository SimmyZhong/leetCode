class Solution:
    def lengthOfLongestSubstring(self, s):
        s_len = len(s)
        if s_len < 2:
            return s_len
        max_len = 1
        for i in range(s_len):
            j = i + max_len
            if j < s_len:
                max_s = s[i:j]
                if 
test_case = "234sdfsgrs"
print(Solution().lengthOfLongestSubstring(test_case))