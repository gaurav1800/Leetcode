func mySqrt(x int) int {

    lo := 0
    hi := x
    
    for (lo <= hi) {
        mid := (lo+hi)/2
        sqrd := mid*mid
        
        if (sqrd > x) {
            hi = int(mid) - 1
        } else if (sqrd < x) {
            lo = int(mid) + 1
        } else {
            return int(mid)
        }
    }
    
    return hi
    
}