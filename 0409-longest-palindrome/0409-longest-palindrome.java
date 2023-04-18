class Solution {
    public int longestPalindrome(String s) {
        
        char[] arr = new char[256];
        int ans = 0;
        
        for(int i=0; i<s.length(); i++) {
            arr[s.charAt(i)]++;
        }
        for(int i=0; i<256; i++) {
            ans += (arr[i]/2); 
        }
        ans *= 2;
        if (ans < s.length()) {
            return ans+1;
        }
        return ans;

        
    }
}