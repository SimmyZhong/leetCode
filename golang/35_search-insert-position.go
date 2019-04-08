package main 

import "fmt"


func searchInsert(nums []int, target int) int {
    low, high := 0, len(nums)
	for low < high {
		fmt.Println(low, high)
		if mid := (high - low) / 2 + low; nums[mid] == target {
			return mid
		} else if nums[mid] < target {
			low = mid + 1
		} else {
			high = mid
		}
	}
	return low
}


func test() {

	fmt.Println(12/5)
}


func firstUniqChar(s string) int {
    var choice [75]int
    for _, word := range(s) {
    	choice[word - '0'] += 1
    }
    for index, word := range(s) {
    	if choice[word - '0'] == 1 {
    		return index
    	}
    }
    return -1
}


func main() {
	fmt.Println(firstUniqChar("09aleetcodez"))
}
