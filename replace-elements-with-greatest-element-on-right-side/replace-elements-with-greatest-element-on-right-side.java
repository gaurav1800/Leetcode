class Solution {
    public int[] replaceElements(int[] arr) {
        
        if (arr.length == 1) {
            arr[0] = -1;
            return arr;
        }
        
        int max = -1;
        
        for(int i=arr.length-1; i>-1; i--) {
            int temp = arr[i];
            
            arr[i] = max;
            
            if (temp > max) {
                max = temp;
            }
        }
        arr[arr.length-1] = -1;
        return arr;
        
    }
}