from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        
        myCounter = Counter(nums)
        
        result = myCounter.most_common(k)
        
        result = [num for num, _ in result]
        
        return result
        