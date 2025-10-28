class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        counter = 0
        currentNum = 0

        for num in nums:
            if counter == 0:
                currentNum = num
            if currentNum == num:
                counter += 1
            else:
                counter -= 1
        return currentNum