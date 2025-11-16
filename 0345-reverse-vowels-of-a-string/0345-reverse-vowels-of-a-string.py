class Solution:
    def reverseVowels(self, s: str) -> str:
        
        vowelSet = {'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'}
        s_list = list(s)

        lo, hi = 0, len(s_list)-1

        while lo < hi:
            while lo < hi and s_list[lo] not in vowelSet:
                lo += 1
            while lo < hi and s_list[hi] not in vowelSet:
                hi -= 1
            if lo >= hi:
                break
            s_list[lo], s_list[hi] = s_list[hi], s_list[lo]
            lo += 1
            hi -= 1
        
        return ''.join(s_list)