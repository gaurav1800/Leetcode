class Solution {
public:
    string reverseWords(std::string s) {
        
        string result="";
        
        string temp="";

        
        for(int i = s.size()-1 ; i >= 0; i--)
        {
            if(s[i] != ' ')
            {
                temp += s[i];
            }
            
            else if(!temp.empty()) {
                reverse(temp.begin(), temp.end());
                
                if(!result.empty()){
                    result += " ";
                }
                
                result += temp;
                temp = "";
            }
        }
        
        if(!temp.empty()){
            
            reverse(temp.begin(), temp.end());
            
            if(!result.empty()){
                result += " ";
            }
            
            result += temp;
            
        }
        
        return result;
        
    }
};
