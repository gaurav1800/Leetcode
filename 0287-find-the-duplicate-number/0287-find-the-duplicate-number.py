class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        res = set()
        
        for num in nums:
            if num not in res:
                res.add(num)
            else:
                return num
        