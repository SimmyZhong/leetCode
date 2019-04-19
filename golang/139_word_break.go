package main

import "fmt"

func main() {
	fmt.Println(wordBreak("catsandog", []string{"cats", "dog", "sand", "and", "cat"}))
}

func wordBreak(s string, wordDict []string) bool{
	result := []int{0}
	for idx := range s {
		LABEL:
		for _, idy := range result {
			for _, word := range wordDict {
				if s[idy: idx+1] == word {
					result = append(result, idx+1)
					break LABEL
				}
			}
		}
	}
	if result[len(result)-1] == len(s) {
		return true
	}
	return false
}