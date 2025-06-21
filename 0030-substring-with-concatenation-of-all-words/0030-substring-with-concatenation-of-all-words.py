class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        if len(s) == 0 or len(words) == 0:
            return []

        m = len(words[0])
        n = len(words)
        result = []
        counter = collections.Counter(words)

        for i in range(len(s) - n * m + 1):
            seen = collections.defaultdict(int)
            j = 0
            while j < n:
                word = s[i + j * m: i + j * m + m]
                seen[word] += 1
                if seen[word] > counter[word]:
                    break
                j += 1
            if j == n:
                result.append(i)

        return result