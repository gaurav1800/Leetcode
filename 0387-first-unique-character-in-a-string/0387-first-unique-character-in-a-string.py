class Solution:
    def firstUniqChar(self, s: str) -> int:
        
#         slow solution
        # for idx, char in enumerate(s):
        #     if s.count(char) == 1:
        #         return idx;
        # return -1
        
#         faster solution
        map = {}

        for char in s:
            if char not in map:
                map[char] = 1
            else:
                map[char] += 1

        for idx, char in enumerate(s):
            if map[char] == 1:
                return idx

        return -1