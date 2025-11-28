class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        
        # reverse list
        nums[:len(nums)] = nums[:len(nums)][::-1]
        
        # reverse 2 parts
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]
        