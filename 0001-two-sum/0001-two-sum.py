class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
#         slow implementation
        # for idx,num in enumerate(nums):
        #     if target-num in nums:
        #         if num + nums[nums.index(target-num)] == target and idx != nums.index(target-num):
        #             return [idx, nums.index(target-num)]

        # faster implementation
        prevMap = {} 
        for idx, val in enumerate(nums):
            diff = target - val
            if diff in prevMap:
                return [prevMap[diff], idx]
            else:
                prevMap[val] = idx