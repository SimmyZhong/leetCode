"""
https://leetcode-cn.com/problems/insert-interval/
给出一个无重叠的 ，按照区间起始端点排序的区间列表。

在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。

示例 1:

输入: intervals = [[1,3],[6,9]], newInterval = [2,5]
输出: [[1,5],[6,9]]
示例 2:

输入: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
输出: [[1,2],[3,10],[12,16]]
解释: 这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。
"""


# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def insert(self, intervals, newInterval):
        i = 0
        while i < len(intervals):
            each = intervals[i]
            if self.__can_merge(each, newInterval):
                args = [each.start, each.end, newInterval.start, newInterval.end]
                newInterval = Interval(min(args), max(args))
                intervals.remove(each)
                continue
            elif each.start > newInterval.end:
                intervals.insert(i, newInterval)
                break
            
            i += 1
        if not intervals:
            return [newInterval]
        elif intervals[-1].end < newInterval.start:
            intervals.append(newInterval)
        return intervals


    def __can_merge(self, sec1, sec2):
        """
        判断两个区间是否能合并
        """
        return True if sec1.end >= sec2.start and sec1.start <= sec2.end else False


class Solution2:
    """
    方法2
    """
    def insert(self, intervals, newInterval):
        pointList = [(newInterval.start, 0), (newInterval.end, 1)]
        for each in intervals:
            pointList.append((each.start, 0))
            pointList.append((each.end, 1))
        pointList.sort()
        return self.__getList(pointList)


    def __getList(self, pointList):
        flag = 0
        res = []
        for item in pointList:
            if item[1] == 0:
                flag += 1
                if flag == 1:
                    start = item[0]
            if item[1] == 1:
                flag -= 1
                if flag == 0:
                    end = item[0]
                    res.append([start, end])
        return res