class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dict1: Dict[tuple, List[str]] = {}
        
        for word in strs:
            key = tuple(sorted(word))
            if key in dict1.keys():
                dict1[key].append(word)
            else:
                dict1[key] = [word]
        
        return list(dict1.values())
        