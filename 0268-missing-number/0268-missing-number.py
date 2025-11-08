class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        arr = [-1] * (len(nums) + 1)

        for n in nums:
            arr[n] = n
        
        for idx, num in enumerate(arr):
            if num == -1:
                return idx
        
        return len(arr)
        