class Solution {
public:
    std::string reverseWords(std::string s) {

        
        int start = 0, end = s.size() - 1;
        
        while (start <= end && s[start] == ' ') start++;
        
        while (end >= start && s[end] == ' ') end--;

        
        reverse(s.begin() + start, s.begin() + end + 1);

        int i = start, j = start;
        
        while (i <= end) {
        
            while (j <= end && s[j] != ' ') j++;

            reverse(s.begin() + i, s.begin() + j);

            i = j + 1;
            j = i;
        }

        int slow = start, fast = start;
        
        while (fast <= end) {
        
            while (fast <= end && s[fast] == ' ') fast++;
            
            while (fast <= end && s[fast] != ' ') s[slow++] = s[fast++];
            
            while (fast <= end && s[fast] == ' ') fast++;
            
            if (fast <= end) s[slow++] = ' ';
        }

        return s.substr(start, slow - start);
    }
};
