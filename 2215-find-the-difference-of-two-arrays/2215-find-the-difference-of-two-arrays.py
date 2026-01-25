class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        set1 = set()
        set2 = set()
        set3 = set()
        set4 = set()

        for i in nums1:
            set1.add(i)

        for i in nums2:
            set2.add(i)
            
        for n in set1:
            if n not in set2:
                set3.add(n)
        
        for n in set2:
            if n not in set1:
                set4.add(n)
        
        return [list(set3), list(set4)]


