class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        n = bisect.bisect_left(range(num), num, key = lambda f: f*f)
        return n**2 == num