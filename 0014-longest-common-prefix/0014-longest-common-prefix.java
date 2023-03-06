class Solution {
    public String longestCommonPrefix(String[] strs) {
        
        if (strs.length == 1) {
            return strs[0];
        }
        
        String res = "";
        
        for(int i=0; i<strs[0].length(); i++) {
            int j=1;
            while (j<strs.length && i < strs[j].length() && strs[0].charAt(i) == strs[j].charAt(i)) {
                j++;
            }
            if (j == strs.length) {
                res += strs[0].charAt(i);
            }
            else {
                return res;
            }
        }
        
        return res;
        
    }
}