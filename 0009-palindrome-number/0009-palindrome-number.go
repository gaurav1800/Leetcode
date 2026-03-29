func isPalindrome(x int) bool {

    if x < 0 || (x%10 == 0 && x != 0) {
            return false
    }

    reversed := 0
    orig := x

    for x > 0 {
        reversed = (reversed * 10) + (x % 10)
        x /= 10
    }

    return orig == reversed
    
}