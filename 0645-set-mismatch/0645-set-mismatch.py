class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        arr = [0] * (len(nums)+1)
        
        for num in nums:
            arr[num] += 1
        
        num1 = 0
        num2 = 0
        
        for num in range(1, len(arr)):
            
            if arr[num] == 2:
                num1 = num
                
            if arr[num] == 0:
                num2 = num
        
        return [num1, num2]
            
            
        