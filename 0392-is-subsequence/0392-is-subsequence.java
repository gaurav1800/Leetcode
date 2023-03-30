class Solution {
    public boolean isSubsequence(String s, String t) {
        
        int i=0, j=0;
        int a=s.length(), b=t.length();
        
        if (t.length() < s.length()) {
            return false;
        }
        if(a<1) {
            return true;
        }
        

        
        char[] sarr = s.toCharArray();
        char[] tarr = t.toCharArray();
        
        
        
        while(j < b){
            if (sarr[i] == tarr[j]) {
                i++;
            }
            j++;
            
            if (i==s.length()) {
            return true;
            }
            
        }
        return false;
        
        
    }
}