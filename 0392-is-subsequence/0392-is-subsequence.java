class Solution {
    public boolean isSubsequence(String s, String t) {

        
        char[] sArr = s.toCharArray();
        char[] tArr = t.toCharArray();
        int a = sArr.length;
        int b = tArr.length;
        
        int i=0, j=0;
        while (i!=a && j!=b) {
            if (sArr[i] == tArr[j]) {
                i++;
            }
            j++;
        }
        if (i == a) {
            return true;
        }
        else {
            return false;
        }
        
    }
}