class Solution {
public:
    bool isValid(string s) {
        
        stack<char> stack;
        
        for (char c : s) {
            if (c == '(' || c == '{' || c == '[') {
                stack.push(c);
            }
            else if (!stack.empty() && c == ')' ) {
                if (stack.top() == '(') {
                    stack.pop();
                }
                else {
                    return false;
                }
            }
            else if (!stack.empty() && c == '}' ) {
                if (stack.top() == '{') {
                    stack.pop();
                }
                else {
                    return false;
                }
            }
            else if (!stack.empty() && c == ']' ) {
                if (stack.top() == '[') {
                    stack.pop();
                }
                else {
                    return false;
                }
            }
            else {
                return false;
            }
        }
        
        if (stack.empty()) return true;
        
        return false;
        
    }
};