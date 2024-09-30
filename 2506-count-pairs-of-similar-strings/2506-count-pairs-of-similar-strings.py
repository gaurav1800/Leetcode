class Solution:
    def similarPairs(self, words: List[str]) -> int:
        
        result = 0
        
        for i in range(len(words)-1):
            set1 = set(words[i])
            for j in range(i+1, len(words)):
                if set1 == set(words[j]):
                    result += 1
        return result
        
        