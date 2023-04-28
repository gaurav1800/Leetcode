class Solution {
    public int characterReplacement(String s, int k) {
        
        int res = 0;
        int max = 0;
        int[] counter = new int[128];
        
        for(int i=0, j=0; j < s.length(); j++) {
            max = Math.max(max, ++counter[s.charAt(j)]);
            while (max + k < j - i + 1) {
                --counter[s.charAt(i++)];
            }
            res = Math.max(res, j - i + 1);
        }
        
        return res;
    }
}