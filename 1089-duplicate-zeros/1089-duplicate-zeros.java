class Solution {
    public void duplicateZeros(int[] arr) {
        
        int[] result = new int[arr.length];
        
        int i=0, idx=0;
        
        while(idx<arr.length) {
            if (arr[i] == 0) {
                result[idx] = 0;
                if (idx+1 == result.length) {
                    break;
                }
                result[idx+1] = 0;
                idx++;
            }
            else {
                result[idx] = arr[i];
            }
            i++;
            idx++;
        }
        
        for(int j=0; j<result.length;j++) {
            arr[j] = result[j];    
        }
        
        
    }
}