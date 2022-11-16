import java.io.*;
import java.util.*;

class Solution {
    public boolean isValid(String s) {
        // Stack<Char> stack;
        Stack stack = new Stack();
        
        char[] word = s.toCharArray();
        
        int i = 0;
        
        if (word.length % 2 == 1 || word[0] == ')' || word[0] == ']' || word[0] == '}') {
            return false;
        }
        
        while (i< word.length) {
            if (word[i] == '(' || word[i] == '[' || word[i] == '{') {
                stack.push(word[i]);
            }
            else if (word[i] == ')' && stack.size() > 0 && stack.peek().equals('(')) {
                stack.pop();
            }
            else if (word[i] == ']' && stack.size() > 0 && stack.peek().equals('[')) {
                stack.pop();
            }
            else if (word[i] == '}' && stack.size() > 0 && stack.peek().equals('{')) {
                stack.pop();
            }
            else {
                return false;
            }
            
            i++;
        }
        if (stack.size() == 0) {
            return true;    
        }
        else {
            return false;
        }
        
        
        
    }
}