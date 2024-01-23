class Solution {
    public int strStr(String haystack, String needle) {
        
//         int i = 0;
//         while (i != haystack.length() && needle[i] == haystack[i]) {
            
//             int j = i, k = i;
            
//             while (j != needle.length() && needle[j] == haystack[j]) {
                
//                 j++;
//             }
            
//             if (j == needle.length()) {
//                 return k;
//             }
            
//             i++;
//         }
        
        return haystack.indexOf(needle);
        
    }
}