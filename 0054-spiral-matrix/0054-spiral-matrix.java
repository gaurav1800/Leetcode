class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        
        
        if (matrix.length == 0) {
            return new ArrayList();
        }
        
        int m = matrix.length;
        int n = matrix[0].length;
        
        List<Integer> arr = new ArrayList();
        
        int r1=0, c1=0, r2=m-1, c2=n-1;
        
        
        
        while(arr.size() < m*n) {
            for(int j = c1; j <= c2 && arr.size() < m*n; j++) {
                arr.add(matrix[r1][j]);
            }
            for(int i = r1+1; i <= r2-1 && arr.size() < m*n; i++) {
                arr.add(matrix[i][c2]);
            }
            for(int j = c2; j >= c1 && arr.size() < m*n; j--) {
                arr.add(matrix[r2][j]);
            }
            for(int i = r2-1; i >= r1+1 && arr.size() < m*n; i--) {
                arr.add(matrix[i][c1]);
            }
            r1++;
            c1++;
            r2--;
            c2--;
        }
        
        return arr;
        
    }
}