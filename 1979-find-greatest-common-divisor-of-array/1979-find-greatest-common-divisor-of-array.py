class Solution:
    def findGCD(self, nums: List[int]) -> int:
        
        smallest = min(nums)
        largest = max(nums)
        
        n = smallest
        
        if smallest == largest:
            return smallest
        
        while smallest%n != 0 or largest%n != 0:
            n -= 1
        
        return n
        