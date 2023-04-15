class Solution {
    public boolean isIsomorphic(String s, String t) {
        
        if (s.length() != t.length()) {
            return false;
        }
        
        int[] map1 = new int[256];
        int[] map2 = new int[256];
        
        for(int i=0; i<s.length(); i++) {
            if (map1[s.charAt(i)] != map2[t.charAt(i)]) {
                return false;
            }
            map1[s.charAt(i)] = i+1;
            map2[t.charAt(i)] = i+1;
        }
        
        return true;
        
        
        
        
        
        // too slow
//         if (s.length() != t.length()) {
//             return false;
//         }
        
//         HashMap<Character, Character> map = new HashMap<>();
        
//         for(int i=0; i<s.length(); i++) {
            
//             if (!map.containsKey(s.charAt(i)) && !map.containsValue(t.charAt(i))) {
//                 map.put(s.charAt(i), t.charAt(i));
//             }
//             else if ((!map.containsKey(s.charAt(i)) && map.containsValue(t.charAt(i))) || (map.containsKey(s.charAt(i)) && !map.containsValue(t.charAt(i)))) {
//                 return false;
//             }
//             else {
//                 if (map.get(s.charAt(i)) != t.charAt(i)) {
//                     return false;
//                 }
//             }
//         }
//         return true;
        
        
        
    }
}