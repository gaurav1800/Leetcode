class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        myDict = {}

        for idx, num in enumerate(numbers):
            if target-num in myDict:
                return [myDict[target-num] + 1, idx+1] 
            else:
                myDict[num] = idx
        return