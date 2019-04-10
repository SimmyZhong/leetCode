// 350. 两个数组的交集 II
// https://leetcode-cn.com/problems/intersection-of-two-arrays-ii/

package main

import "fmt"

func main() {
    
    result := intersect([]int{1, 2, 3, 4, 1}, []int{1,2, 1, 5})
    fmt.Println(result)
}

func intersect(nums1 []int, nums2 []int) []int {
    choice := map[int]int{}
    var result []int
    for _, val := range nums2 {
        choice[val]++
    }
    for _, val := range nums1 {
        if choice[val] > 0 {
            result = append(result, val)
            choice[val]--
    }
    }
    return result
}