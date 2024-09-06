class Solution {
public:
    int strStr(string haystack, string needle) {
        
        if (needle.size() > haystack.size()) {
            return -1;
        }
        
        for(int i = 0; i <= haystack.size() - needle.size(); i++) {
            int j = i;
            int k = 0;
            while (j < haystack.size() && k < needle.size() && haystack[j] == needle[k]) {
                j++;
                k++;
            }
            if (k == needle.size()) {
                return i;
            }
        }
        
        return -1;
        
    }
};