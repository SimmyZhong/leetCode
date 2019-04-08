func mySqrt(x int) int {
    if x == 1 {
        return 1
    }
    left, right := 0, x
    for left + 1 < right {
        mid := (left + right) / 2
        if mid * mid < x {
            left = mid
        } else if mid * mid > x {
            right = mid
        } else {
            return mid
        }
    }
    return left
}