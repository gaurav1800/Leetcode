class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        kv = {}
        
        for i, num in enumerate(nums):
            if target - num in kv.keys():
                return [i, kv[target-num]]
            else:
                kv[num] = i
                
        return []