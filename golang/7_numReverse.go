func reverse(x int) int {
	if isPositve := false; x > 0;{
		isPositve = true
	}
	res, y := 0, abs(x)
	while(x) {
		m := x % 10
		x := x / 10
		res := res * 10 + m
		if res >= 2**31 | (res == 2*31 - 1 && !isPositve) {
			return 0
		}
	}
	if !isPositve {
		return -res
	}
	return res
}