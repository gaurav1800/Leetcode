class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dict = collections.defaultdict(list)
        
        for word in strs:
            key = ''.join(sorted(word))
            dict[key].append(word)
        
        return dict.values()
        
                
        