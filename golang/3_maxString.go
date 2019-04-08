func lengthOfLongestSubstring(s string) int {
    res, cur := 0, ""
    for _, word := range(s) {
        index := strings.Index(cur, string(word))
        if index != -1 {
            if res < len(cur) {
                res = len(cur)
            }
            cur = cur[index+1:]
        }
        cur += string(word)  
    }
    if res > len(cur) {
        return res 
    } else {
        return len(cur)
    }
}