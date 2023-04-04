class Solution {
    public int lengthOfLongestSubstring(String s) {
        
        int n = s.length();
        
        int result = 0;
        
        List<Character> visited =  new ArrayList<Character>();
        
        for(int i=0; i<n; i++) {
            for(int j=i; j<n; j++) {
                if(visited.contains(s.charAt(j))) {
                    visited.clear();
                    break;
                }
                else {
                    visited.add(s.charAt(j));
                    if (result < j - i + 1) {
                        result = j - i + 1;
                    }
                }
            }
        }
        return result;
    }
}