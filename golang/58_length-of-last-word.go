/*
https://leetcode-cn.com/problems/length-of-last-word/
给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。

如果不存在最后一个单词，请返回 0 。

说明：一个单词是指由字母组成，但不包含任何空格的字符串。

示例:

输入: "Hello World"
输出: 5
*/

package main 

import "fmt"

func main() {
	fmt.Println(lengthOfLastWord("hello world "))
}

func lengthOfLastWord(s string) int {
    var res int
    for i:=len(s)-1; i >= 0; i-- {
        cur := s[i]
        if cur != 32 {
            res += 1
        } else if res != 0 {
            break
        }
    }
    return res
}