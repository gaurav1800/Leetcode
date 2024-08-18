class Solution {
public:
    bool isAnagram(string s, string t) {
        
        if (s.size() != t.size()) {
            return false;
        }
        
        vector<int> arr(26, 0);
        
        for(int i=0; i<s.size(); i++) {
            arr[s[i] - 'a']++;
            arr[t[i] - 'a']--;
        }
        
        for(int i = 0; i < arr.size(); i++) {
            if (arr[i] != 0) {
                return false;
            }
        }
        
        return true;
        
//         // takes up more space due to the map
//         unordered_map<char, int> map;
        
//         for(char c:s) {
//             map[c]++;
//         }
        
//         for(char c:t){
//             if(map.find(c) == map.end() || map[c] == 0) {
//                 return false;
//             }    
//             else {
//                 map[c]--;
//             }
//         }
//         return true;
        
        
        
        
    }
};