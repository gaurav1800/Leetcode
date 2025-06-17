class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums: return 0
        
        num_set = set(nums)
        result = 0
        
        for num in num_set:
            if num-1 not in num_set:
                current_num = num
                current_max = 1
                
                while current_num + 1 in num_set:
                    current_max += 1
                    current_num += 1
                result = max(result, current_max)
        
        return result