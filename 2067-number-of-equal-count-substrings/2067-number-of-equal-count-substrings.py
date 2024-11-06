class Solution:
    def equalCountSubstrings(self, s: str, count: int) -> int:
        
        result = 0
        
        for i in range(1, 27):
            m = count * i
            
            if m > len(s):
                break
                
            cnt = Counter()
            y = 0
            
            for j, c in enumerate(s):
                cnt[c] += 1
                y += cnt[c] == count
                y -= cnt[c] == count + 1
                k = j - m
                
                if k >= 0:
                    cnt[s[k]] -= 1
                    y += cnt[s[k]] == count
                    y -= cnt[s[k]] == count - 1
                    
                result += i == y
        return result
        