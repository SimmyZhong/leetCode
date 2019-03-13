import random


class Sort:
    """
    数组排序算法
    """
    def mergeSort(self, numList):
        """
        归并排序
        """
        if len(numList) <= 1:
            return numList
        middle = len(numList) // 2
        leftList, rightList = numList[:middle], numList[middle:]
        return self.__mergeList(self.mergeSort(leftList), self.mergeSort(rightList))

    def __mergeList(self, leftList, rightList):
        """
        合并列表
        """

        result = []
        while(len(leftList) > 0 and len(rightList) > 0):
            if leftList[0] < rightList[0]:
                result.append(leftList[0])
                leftList.pop(0)
            else:
                result.append(rightList[0])
                rightList.pop(0)
        if len(leftList):
            result.extend(leftList)
        else:
            result.extend(rightList)
        return result

    def quickSort(self, numList):
        """
        快速排序
        """
        if len(numList) <= 1:
            return numList
        middle = numList.pop(0)
        leftList, rightList = [], []
        for each in numList:
            if each < middle:
                leftList.append(each)
            else:
                rightList.append(each)
        result = self.quickSort(leftList)
        result.append(middle)
        result.extend(self.quickSort(rightList))
        return result


def testCase():
    testList1 = [random.choice(range(100)) for _ in range(10)]
    assert(sorted(testList1) == Sort().mergeSort(testList1))
    assert(sorted(testList1) == Sort().quickSort(testList1))
    print("Test OK")


if __name__ == "__main__":
    testCase()    
    



