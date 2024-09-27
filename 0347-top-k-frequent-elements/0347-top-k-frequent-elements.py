class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dict1 = {}
        
        for num in nums:
            if num in dict1:
                dict1[num] += 1
            else:
                dict1[num] = 1
            
        min_heap = []
        
        for num, freq in dict1.items():
            heapq.heappush(min_heap, (freq, num))
            
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        result = []
        
        for freq, num in min_heap:
            result.append(num)
        
        return result
        
        
        