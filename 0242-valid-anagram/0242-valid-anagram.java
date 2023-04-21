class Solution {
    public boolean isAnagram(String s, String t) {
        
        if (s.length() != t.length()) {
            return false;
        }
        
        int[] arr = new int[26];
        char[] sArr = s.toCharArray();
        char[] tArr = t.toCharArray();
        
        for(int i=0; i < s.length(); i++) {
            arr[sArr[i] - 'a']++;
            arr[tArr[i] - 'a']--;
        }
        
        for(int i=0; i < 26; i++) {
            if (arr[i] != 0) {
                return false;
            }
        }
        
        return true;
        
    }
}