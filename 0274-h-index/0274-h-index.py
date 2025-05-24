class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        citations.sort()
        n = len(citations)
        
        for i, number in enumerate(citations):
            if number >= n - i:
                return n - i
        return 0