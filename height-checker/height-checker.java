class Solution {
    public int heightChecker(int[] heights) {
        
        
        int[] sorted = new int[heights.length];
        
        for(int i=0; i< heights.length; i++) {
            sorted[i] = heights[i];
        }
        
        int counter = 0;
        
        for(int i=1; i<sorted.length; i++) {
            int j = i;
            int key = sorted[i];
            while (j > 0 && sorted[j-1] > key) {
                sorted[j] = sorted[j-1];
                j--;
            }
            sorted[j] = key;
        }
        
        for(int i=0; i< heights.length; i++) {
            if (heights[i] != sorted[i]) {
                counter++;
            }
        }
        
        return counter;
        
    }
}