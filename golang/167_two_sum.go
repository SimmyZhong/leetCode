// https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/
// 给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。
// 函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。
// 说明:
// 返回的下标值（index1 和 index2）不是从零开始的。
// 你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
// 示例:
// 输入: numbers = [2, 7, 11, 15], target = 9
// 输出: [1,2]
// 解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。


// 算法复杂度为O(nlogn)
func twoSum(numbers []int, target int) []int {
    for index, val := range numbers {
        remain := target - val
        left, right := 1, len(numbers) - 1
        for left <= right {
            mid := (left + right) / 2
            mid_val := numbers[mid]
            if remain == mid_val {
                return []int{index + 1, mid + 1}
            } else if remain < mid_val {
                right = mid - 1
            } else {
                left = mid + 1
            }
        }
    }
    return []int{}
}

// 算法复杂度为O(n)
func twoSum(numbers []int, target int) []int {
    i,j := 0 ,  len(numbers) -1
    // var result []int
    // result = make( []int,2)
    for {
        sum:= numbers[i] + numbers[j]
        if sum == target{
            return []int{i+1,j+1}
        }else if sum > target{
            j = j-1
        }else{
            i = i +1
        }
    }
    
}