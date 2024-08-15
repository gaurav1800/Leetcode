class Solution {
public:
    bool isAnagram(string s, string t) {
        
        if (s.size() != t.size()) {
            return false;
        }
        
//         // little bit slower
//         string sortedS = s;
//         string sortedT = t;
        
//         sort(sortedS.begin(), sortedS.end());
//         sort(sortedT.begin(), sortedT.end());
        
//         return sortedS == sortedT;
        
        unordered_map<char, int> map;
        
        for (char c: s) {
            map[c]++;
        }
        
        for (char c: t) {
            if (map.find(c) == map.end() || map[c] == 0) {
                return false;
            }
            else {
                map[c]--;
            }
        }
        return true;
    }
};