class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        rows = len(image)
        cols = len(image[0])
        
        def reverse(arr):
            left, right = 0, len(arr)-1
            
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
            return arr
        
        for row in image:
            reverse(row)
        
        for i in range(rows):
            for j in range(cols):
                image[i][j] = 0 if image[i][j] == 1 else 1
        
        return image