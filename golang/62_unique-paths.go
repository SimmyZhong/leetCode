package main

func main() {
    uniquePaths(2,2)    
}

func uniquePaths(m int, n int) int {
    var choice [][]int
    for i:=0; i < m; i++ {
        choice = append(choice, make([]int, n))
    }
    for i:=0; i < m ; i++ {
        for j:=0; j < n; j++ {
            if i!=0 && j!=0 {
                choice[i][j] = choice[i-1][j] + choice[i][j-1]
            } else {
                choice[i][j] = 1
            }

        }
    }
    return choice[m-1][n-1]
}