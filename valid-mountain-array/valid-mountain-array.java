class Solution {
    public boolean validMountainArray(int[] arr) {
        
        if (arr.length < 3 || arr[1] < arr[0]) {
            return false;
        }
        
        int i = 0;
        
        boolean end = false;
        
        while(i < arr.length-1 && (arr[i] < arr[i+1])) {
            i++;
        }
        
        while(i < arr.length-1 && (arr[i] > arr[i+1])) {
            if (i+1 == arr.length-1) {
                end = true;
            }
            i++;
        }
        
        
        if (end == true) {
            return true;
        }
        else {
            return false;
        }
        
    }
}