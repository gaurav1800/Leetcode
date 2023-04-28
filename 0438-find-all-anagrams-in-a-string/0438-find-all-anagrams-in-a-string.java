class Solution {
    public List<Integer> findAnagrams(String s, String p) {

        if (p.length() > s.length()) {
            return new ArrayList();
        }
        
        List<Integer> result = new ArrayList();
        
        HashMap<Integer, String> map = new HashMap();
        
        for(int i=0; i < s.length()-p.length()+1; i++) {
            map.put(i, s.substring(i, i+p.length()));
        }
        
        for(int i=0; i<s.length()-p.length()+1; i++) {
            if (map.containsKey(i) && isAnagram(map.get(i), p)) {
                result.add(i);
            } 
        }
        
        return result;
        
        
        
                
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
    
    
    
    
    
    
    
    
    
//          // Another Solution        
//         int slen = s.length(), plen = p.length();
        
//         if (slen < plen) return new ArrayList();
        
//         int[] scounter = new int[26];
//         int[] pcounter = new int[26];
        
//         for(char c : p.toCharArray()) {
//             pcounter[(int)(c - 'a')]++;
//         }
        
//         List<Integer> result = new ArrayList();
        
//         for(int i=0; i<slen; i++) {
//             scounter[(int) (s.charAt(i) - 'a')]++;
            
//             if (i >= plen) {
//                 scounter[(int) (s.charAt(i-plen) - 'a')]--;
//             }
            
//             if (Arrays.equals(pcounter, scounter)) {
//                 result.add(i-plen+1);
//             }
//         }
        
//         return result;
//     }
        
        
        
    
//         // Another Solution
//         List<Integer> list = new ArrayList<>();
        
//         for(int i=0; i<s.length()-p.length()+1; i++) {
//             if (isAnagram(p, s.substring(i, i+p.length()))) {
//                 list.add(i);
//             }
//         }
//         return list;
        
//     }
    
//     public boolean isAnagram(String p, String s) {
//         int[] arr = new int[128];
        
//         for(int i=0; i<p.length(); i++) {
//             arr[p.charAt(i)]++;
//         }
        
//         for(int i=0; i<s.length(); i++) {
//             arr[s.charAt(i)]--;
//             if (arr[s.charAt(i)] < 0) {
//                 return false;
//             }
//         }
//         return true;
//     }
}