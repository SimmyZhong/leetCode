
import sys, string
# class Solution:
#     def coinChange(self, nums, target):
#         resp =[0] * (target+1)
#         for i in range(1, target+1):
#             cur = sys.maxsize
#             for each in nums:
#                 if i - each >= 0:
#                     cur = min(resp[i-each]+1, cur)
#             resp[i] = cur 
#         return resp[target] if resp[target] != sys.maxsize else -1

# print(Solution().coinChange([2],3))


def test(a, b):
    choice = dict(zip('0123456789'+string.ascii_lowercase, range(36)))
    choice2 = dict(zip(range(36), '0123456789'+string.ascii_lowercase))
    len_a, len_b = len(a), len(b)
    lens = len_a+1 if len_a > len_b else len_b+1
    resp = [0] * lens
    flag = False
    for i in range(lens):
        if len_a - i > 0:
            resp[i] += choice[a[len_a-i-1]]
        if len_b - i > 0:
            resp[i] += choice[b[len_b-i-1]]
        if flag:
            resp[i] += 1
        if resp[i] > 35:
            resp[i] -= 35
            flag = True
        else:
            flag = False
        resp[i] = choice2[resp[i]]
    return ''.join(resp)

# print(test('abc', 'adb'))

def test(s):
    if not s:
        return 0
    i, resp, mapping = 0, 0, {}
    for j in range(len(s)):
        word = s[j]
        if word in mapping and mapping[word] >= i:
            resp = max(j-i, resp)
            i = mapping[word] + 1
        mapping[word] = j
    return max(resp, j-i+1)

print(test('abca'))