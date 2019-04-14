func minimumTotal(triangle [][]int) int {
    minLen := triangle[len(triangle)-1]
    for i:=len(triangle)-2; i >= 0; i-- {
        for j:=0; j < len(triangle[i]); j++ {
                minLen[j] = minLen[j+1] + triangle[i][j]
            }
        }
        minLen = minLen[:len(minLen)-1]
    }
    return minLen[0]
}