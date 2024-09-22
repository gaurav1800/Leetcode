class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if not s:
            return ""
        
        left = 0
        right = 0
        
        for i in range(len(s)):
            len1 = self.expand(s, i, i)
            len2 = self.expand(s, i, i+1)
            result = max(len1, len2)
            
            if result > right - left + 1:
                left = i - (result-1)//2
                right = i + result//2
        
        return s[int(left):int(right+1)]
        
        
    def expand(self, word, left, right):
        while 0 <= left and right < len(word) and word[left] == word[right]:
            left -= 1
            right += 1

        return right - left - 1
        