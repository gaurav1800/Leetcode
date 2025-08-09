class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        counter = 0
        currentNum = 0

        for n in nums:
            if counter == 0:
                currentNum = n
            if currentNum == n:
                counter += 1
            else:
                counter -= 1
        return currentNum