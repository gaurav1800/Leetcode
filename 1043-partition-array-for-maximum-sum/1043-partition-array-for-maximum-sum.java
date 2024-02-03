class Solution {
    public int maxSumAfterPartitioning(int[] arr, int k) {
        
        int n = arr.length;
        int[] result = new int[n + 1];
        
        for (int i = 1; i <= n; i++) {
            int max = Integer.MIN_VALUE;
            
            for (int j = 1; j <= Math.min(i, k); j++) {
                max = Math.max(max, arr[i - j]);
                result[i] = Math.max(result[i], result[i - j] + max * j);
            }
        }
        
        return result[n];
    }
}
