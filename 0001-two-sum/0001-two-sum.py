class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dict1 = {}
        
        for i in range(len(nums)):
            if target - nums[i] in dict1.keys():
                return [i, dict1[target-nums[i]]]
            else:
                dict1[nums[i]] = i
                
        return []
        