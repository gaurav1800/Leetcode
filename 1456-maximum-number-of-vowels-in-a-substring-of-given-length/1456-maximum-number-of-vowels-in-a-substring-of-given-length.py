class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        vowelSet = set(['a', 'e', 'i', 'o', 'u'])
        result = 0
        currentCount = 0

        i = 0
        while i < k:
            if s[i] in vowelSet:
                currentCount += 1
                result = max(result, currentCount)
            i += 1
        
        l, r = 0, k-1
        length = len(s)

        while r < length:
            l += 1
            r += 1
            if r == length:
                break
            if s[l-1] in vowelSet and s[r] not in vowelSet:
                currentCount -= 1
            elif s[l-1] not in vowelSet and s[r] in vowelSet:
                currentCount += 1
                result = max(result, currentCount)
        
        return result


            



        