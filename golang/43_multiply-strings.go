/*
https://leetcode-cn.com/problems/multiply-strings/
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

示例 1:

输入: num1 = "2", num2 = "3"
输出: "6"
示例 2:

输入: num1 = "123", num2 = "456"
输出: "56088"
说明：

num1 和 num2 的长度小于110。
num1 和 num2 只包含数字 0-9。
num1 和 num2 均不以零开头，除非是数字 0 本身。
不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。
*/

package main

import (
    "fmt"
    "strconv"
)

func main() {
    fmt.Println(456789*987654)
    fmt.Println([]rune("abc"), []byte("abc"))
    fmt.Println(multiply("456789","987654"))
}

func multiply(num1, num2 string) string {
    if num1 == "0" || num2 == "0" {
        return "0"
    }
    len1, len2 := len(num1), len(num2)
    choice := make([]int, len1+len2)
    for i := len1-1; i >=0; i-- {
        for j:= len2-1; j >= 0; j-- {
            choice[i+j+1] += int((num1[i] - '0') * (num2[j] - '0'))
        }
    }
    var res string
    var cur int
    for i := len1+len2-1; i >= 0; i-- {
        choice[i] += cur
        cur = choice[i] / 10
        choice[i] %= 10
    }
    for _, each := range choice {
        res = res + strconv.Itoa(each)
    }
    if res[0] == '0' {
        return res[1:]
    } else{
        return res
    }
}