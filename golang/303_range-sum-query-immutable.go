/*
https://leetcode-cn.com/problems/range-sum-query-immutable/
给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。

示例：

给定 nums = [-2, 0, 3, -5, 2, -1]，求和函数为 sumRange()

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
说明:

你可以假设数组不可变。
会多次调用 sumRange 方法。
*/

package main

import "fmt"

type NumArray struct {
	nums []int
	sumList []int
	lens int
}

func main () {
	nums := []int{}
	result := Constructor(nums)
	fmt.Println(result.SumRange(0,5))
}

func Constructor(nums []int) NumArray {
	var res NumArray
	res.nums, res.lens = nums, len(nums)
	if res.lens == 0 {
		return res
	}
	res.sumList = append(res.sumList, nums[0])
	for i:=1; i < res.lens; i++ {
		res.sumList = append(res.sumList, nums[i]+res.sumList[i-1])
	}
	return res
}

func (this *NumArray) SumRange(i, j int) int {
	// 动态规划法：对于nums的和sumList,有sumList[n] = sumList[n-1] + nums[n]
	if i >= this.lens {
		return 0
	}
	return this.sumList[j] - this.sumList[i] + this.nums[i]
}

