class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        
        if (image[sr][sc] == color) return image;
        
        fill(image,sr,sc,image[sr][sc], color);
        return image;
        
//         // slower
//         int oldColor = image[sr][sc];
        
//         if (oldColor == color) {
//             return image;
//         }
        
//         int[][] grid = new int[][]{{0,1},{0,-1},{1,0},{-1,0}};
//         image[sr][sc] = color;
        
//         for(int i=0; i<grid.length; i++) {
//             int nxtX = sr + grid[i][0];
//             int nxtY = sc + grid[i][1];
//             if (nxtX < 0 || nxtX >= image.length || nxtY < 0 || nxtY >= image[0].length) {
//                 continue;
//             }
//             if (image[nxtX][nxtY] != oldColor) {
//                 continue;
//             }
//             floodFill(image, nxtX, nxtY, color);
//         }
        
//         return image;
        
        
    }
    
    public void fill(int[][] image, int i, int j, int oldColor, int newColor) {
        if (i<0 || j<0 || i>image.length-1 || j>image[0].length-1 || image[i][j] != oldColor) {
            return;
        }
        image[i][j] = newColor;
        fill(image, i-1, j, oldColor, newColor);
        fill(image, i, j-1, oldColor, newColor);
        fill(image, i+1, j, oldColor, newColor);
        fill(image, i, j+1, oldColor, newColor);
    }
}


