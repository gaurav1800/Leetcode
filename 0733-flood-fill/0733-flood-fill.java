class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        
        if (image[sr][sc] == color) return image;
        
        fill(image,sr,sc,image[sr][sc], color);
        return image;
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


