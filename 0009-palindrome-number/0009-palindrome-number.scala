import scala.annotation.tailrec

object Solution {
    def isPalindrome(x: Int): Boolean = {
        if (x < 0 || x % 10 == 0 && x != 0) {
            false
        } else {
            @tailrec
            def reverse(currentX: Int, currentReversed: Int): Int = {
                if (currentX == 0) {
                    currentReversed
                } else {
                    val lastDigit = currentX % 10
                    val nextReversed = (currentReversed * 10) + lastDigit
                    reverse(currentX / 10, nextReversed)
                }
            }
            reverse(x, 0) == x
        }
        
    }
}