class Solution {
    public int lengthOfLastWord(String s) {
        
        char[] arr = s.toCharArray();
        
        int num = arr.length, i = num-1;
        
        while (arr[i] == ' ') {
            i--;
        }
        
        int j = i;
        
        
        while (i >= 0 && arr[i] != ' ') {
            i--;
        }
        
        
        
        int k = j-i;
        
        return k;
            
            
    }
}