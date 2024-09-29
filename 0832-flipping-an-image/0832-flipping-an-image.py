class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        rows = len(image)
        cols = len(image[0])
        
        for row in image:
            row.reverse()
        
        for i in range(rows):
            for j in range(cols):
                image[i][j] = 0 if image[i][j] == 1 else 1
        
        return image