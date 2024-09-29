class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        
        nums.sort()
        
        prefix_sum = list(accumulate(nums))
        
        n = len(nums)
        result = []
        
        for query in queries:
            pos = bisect_left(nums, query)
            left_operations = query * pos - (prefix_sum[pos-1] if pos > 0 else 0)
            right_operations = (prefix_sum[-1] - (prefix_sum[pos-1] if pos > 0 else 0)) - query * (n-pos)
            result.append(left_operations + right_operations)
        
        return result
            
            
            
        