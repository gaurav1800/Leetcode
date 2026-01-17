class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        result = 0
        i = 0
        for n in gain:
            i += n
            result = result if result > i else i
        return result
