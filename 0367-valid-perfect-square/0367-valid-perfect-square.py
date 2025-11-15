class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        if num == 1:
            return True
        
        lo, hi = 2, num//2

        while lo <= hi:
            mid = (lo + hi) // 2
            midSquared = mid ** 2
            if midSquared == num:
                return True
            elif midSquared < num:
                lo = mid + 1
            else:
                hi = mid - 1
        
        return False