class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        kv = {}
        occSet = set()

        for num in arr:
            if num not in kv:
                kv[num] = 1
            else:
                kv[num] += 1
        
        for val in kv.values():
            if val in occSet:
                return False
            occSet.add(val)

        return True
