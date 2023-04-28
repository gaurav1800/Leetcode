class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        
        List<Integer> list = new ArrayList<>();
        
        for(int i=0; i<s.length()-p.length()+1; i++) {
            if (isAnagram(p, s.substring(i, i+p.length()))) {
                list.add(i);
            }
        }
        return list;
        
    }
    
    public boolean isAnagram(String p, String s) {
        int[] arr = new int[128];
        
        for(int i=0; i<p.length(); i++) {
            arr[p.charAt(i)]++;
        }
        
        for(int i=0; i<s.length(); i++) {
            arr[s.charAt(i)]--;
            if (arr[s.charAt(i)] < 0) {
                return false;
            }
        }
        return true;
    }
}