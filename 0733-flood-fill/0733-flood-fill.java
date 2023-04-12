class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        
        int oldColor = image[sr][sc];
        
        if (oldColor == color) {
            return image;
        }
        
        int[][] grid = new int[][]{{0,1},{0,-1},{1,0},{-1,0}};
        image[sr][sc] = color;
        
        for(int i=0; i<grid.length; i++) {
            int nxtX = sr + grid[i][0];
            int nxtY = sc + grid[i][1];
            if (nxtX < 0 || nxtX >= image.length || nxtY < 0 || nxtY >= image[0].length) {
                continue;
            }
            if (image[nxtX][nxtY] != oldColor) {
                continue;
            }
            floodFill(image, nxtX, nxtY, color);
        }
        
        return image;
        
        
    }
}