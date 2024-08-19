class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        
        
        vector<vector<string>> result;
        
        unordered_map<string, vector<string>> map;
        
        for(string & str: strs) {
            string key = str;
            
            sort(key.begin(), key.end());
            
            map[key].push_back(str);
        }
        
        for(auto [_, anagrams] : map) {
            result.push_back(anagrams);
        }
        
        return result;
    }
                 
};