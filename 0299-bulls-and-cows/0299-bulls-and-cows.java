class Solution {
    public String getHint(String secret, String guess) {
        
        char[] s = secret.toCharArray();
        char[] g = guess.toCharArray();
        char[] sArray = new char[10];
        char[] gArray = new char[10];
        int bulls=0, cows=0;
        
        for(int i=0; i<s.length; i++) {
            if (s[i] == g[i]) {
                bulls++;
            }
            else {
                sArray[s[i] - '0']++;
                gArray[g[i] - '0']++;
            }
        }
        
        for(int i=0; i<10; i++) {
            cows += Math.min(sArray[i], gArray[i]);
        }
        
        return String.valueOf(bulls) + 'A' + String.valueOf(cows) + 'B';
        
    }
}