class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        
        HashMap<Character, Integer> letters = new HashMap<>();
        
        for(int i=0; i < magazine.length(); i++) {
            char c = magazine.charAt(i);
            
            int count = letters.getOrDefault(c, 0);
            
            letters.put(c, count+1);
        }
        
        for(int i=0; i < ransomNote.length(); i++) {
            char c = ransomNote.charAt(i);
            
            int count = letters.getOrDefault(c, 0);
            
            if(count == 0) {
                return false;
            }
            
            letters.put(c, count-1);
        }
        return true;
        
    }
}