class Solution:
    def firstUniqChar(self, s: str) -> int:
        
# #         slow solution
        # for idx, char in enumerate(s):
        #     if s.count(char) == 1:
        #         return idx;
        # return -1
        
# #         faster solution
#         map = {}

#         for char in s:
#             if char not in map:
#                 map[char] = 1
#             else:
#                 map[char] += 1

#         for idx, char in enumerate(s):
#             if map[char] == 1:
#                 return idx

#         return -1
    
    
        letter='abcdefghijklmnopqrstuvwxyz'
        index=[s.index(l) for l in letter if s.count(l) == 1]
        return min(index) if len(index) > 0 else -1