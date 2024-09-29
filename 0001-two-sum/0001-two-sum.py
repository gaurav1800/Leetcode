class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dict1 = {}
        
        for i, num in enumerate(nums):
            if target - num in dict1.keys():
                return [i, dict1[target-num]]
            else:
                dict1[num] = i
                
        return []
        