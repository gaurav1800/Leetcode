class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        if len(s) == 0 or len(words) == 0:
            return []

        n = len(words[0])
        m = len(words)
        map1 = {}
        
        for word in words:
            if word not in map1:
                map1[word] = 1
            else:
                map1[word] += 1
        result = []
        for i in range(len(s) - m * n + 1):
            map2 = {}
            for j in range(m):
                sub = s[i + j * n:i + (j+1) * n]
                if sub not in map1:
                    break
                if sub not in map2:
                    map2[sub] = 1
                else:
                    map2[sub] += 1
            if map1 == map2:
                result.append(i)
        return result