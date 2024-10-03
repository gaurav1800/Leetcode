class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        
        for region in regions[::-1]:
            if region1 in region and region2 in region:
                return region[0]
            elif region1 in region:
                region1 = region[0]
            elif region2 in region:
                region2 = region[0]
        
        for region in regions:
            if region1 in region and region2 in region:
                return region[0]
        
        return True
            
                
        