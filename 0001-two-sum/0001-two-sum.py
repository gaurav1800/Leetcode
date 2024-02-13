class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for idx,num in enumerate(nums):
            if target-num in nums:
                if num + nums[nums.index(target-num)] == target and idx != nums.index(target-num):
                    return [idx, nums.index(target-num)]
