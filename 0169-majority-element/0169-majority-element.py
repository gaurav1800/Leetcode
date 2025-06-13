class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        counter = 0
        num = 0

        for n in nums:
            if counter == 0:
                num = n
            if num == n:
                counter += 1
            else:
                counter -= 1
        return num