class Solution:
    def frequencySort(self, s: str) -> str:
        
        result = []
        
        buckets = [[] for _ in range(len(s) + 1)]
        
        for c, freq in collections.Counter(s).items():
            buckets[freq].append(c)
            
        for freq in reversed(range(len(buckets))):
            for c in buckets[freq]:
                result.append(c*freq)
        
        
        return ''.join(result)
        