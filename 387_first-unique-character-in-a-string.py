class Solution:
    def firstUniqChar(self, s: str) -> int:
        choice = list()
        for each in s:
        	choice[ord(each)] += 1
        for each in s:
        	if choice[ord(each)] == 1:
        		return ord(each)
        return -1
