class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        
        nums.sort()
        
        result = []
        
        n = len(nums)
        
        for i in range(0, n, 3):
            j = nums[i:i+3]
            if j[2] - j[0] > k:
                return []
            result.append(j)
        
        return result