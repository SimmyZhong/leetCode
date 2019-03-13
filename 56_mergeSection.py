"""
给出一个区间的集合，请合并所有重叠的区间。

示例 1:

输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2:

输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
"""


# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:

    def merge(self, intervals):
        result = []
        if not intervals:
            return result
        cur_sec = intervals.pop(0)
        while True:
            if not intervals:
                result.append(cur_sec)
                break
            for each in intervals:
                if self.__can_merge(cur_sec, each):
                    args = [each.start, each.end, cur_sec.start, cur_sec.end]
                    cur_sec = Interval(min(args), max(args))
                    intervals.remove(each)
                    break
                if each == intervals[-1]:
                    result.append(cur_sec)
                    cur_sec = intervals.pop(0)
        return result

    def __can_merge(self, sec1, sec2):
        """
        判断两个区间是否能合并
        """
        return True if sec1.end >= sec2.start and sec1.start <= sec2.end else False


def test_case():
    origin_list = [[1, 3], [2, 6], [8, 10], [15, 18]]
    test_list = [Interval(each[0], each[1]) for each in origin_list]
    assert([[1, 6], [8, 10], [15, 18]] == [[each.start, each.end] for each in Solution().merge(test_list)])
    assert([] == Solution().merge([]))
    print("Test OK")


if __name__ == "__main__":
    test_case()
