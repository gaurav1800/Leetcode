class Solution:
    def frequencySort(self, s: str) -> str:
        
        freq_map = {}
        for char in s:
            freq_map[char] = freq_map.get(char, 0) + 1
        new_str = ''
        for char in sorted(freq_map, key=lambda x: freq_map[x], reverse=True):
            new_str += char * freq_map[char]
        return new_str 