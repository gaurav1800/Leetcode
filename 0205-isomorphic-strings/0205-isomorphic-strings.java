class Solution {
    public boolean isIsomorphic(String s, String t) {
        
        int a=s.length(), b=t.length();
        
        
        if (a != b) {
            return false;
        }
        if(s.equals(t)) {
            return true;
        }
        
        
        
        //int size = 256;
        Boolean[] done = new Boolean[256];
        Arrays.fill(done, Boolean.FALSE);
        
        int[] map = new int[256];
        Arrays.fill(map,-1);
        
        for(int i=0; i<b; i++) {
            if(map[s.charAt(i)] == -1) {
                if(done[t.charAt(i)] == true) {
                    return false;
                }
                done[t.charAt(i)] = true;
                map[s.charAt(i)] = t.charAt(i);
            }
            
            else if (map[s.charAt(i)] != t.charAt(i)){
                return false;
            }
        }
        
        return true;
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
//         HashMap<Character, Integer> map1 = new HashMap<>();
//         HashMap<Character, Integer> map2 = new HashMap<>();
        
//         int i=0, j=0;
//         while(i != s.length()) {
//             if (map1.containsKey(s.charAt(i))) {
//                 map1.put(s.charAt(i), map1.get(s.charAt(i)));
//             }
//             else {
//                 map1.put(s.charAt(i), j);
//                 j++;
//             }
//             i++;
//         }
        
//         i=0;
//         j=0;
//         while(i != t.length()) {
//             if (map2.containsKey(t.charAt(i))) {
//                 map2.put(t.charAt(i), map2.get(t.charAt(i)));
//             }
//             else {
//                 map2.put(t.charAt(i), j);
//                 j++;
//             }
//             i++;
//         }
        
//         if (map1.values().equals(map2.values())) {
//             return true;
//         }
//         else {
//             return false;
//         }
        
        
        
    }
}