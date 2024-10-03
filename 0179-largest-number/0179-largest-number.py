class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        strs = [str(x) for x in nums]
        
        def compare(x, y):
            if x+y > y+x:
                return -1  # keep x before y
            elif x+y < y+x:
                return 1   # keep y before x
            else:
                return 0
        
        strs.sort(key = cmp_to_key(compare))
        
        result = "".join(strs)
        
        if result[0] == "0":
            return "0"
        else:
            return result