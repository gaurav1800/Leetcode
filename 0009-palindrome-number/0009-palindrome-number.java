class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0) {
            return false;
        }
        
        long q, remaining=x, result=0;
        
        while (remaining != 0) {
            q = remaining % 10; 
            remaining /= 10;
            
            if (q==0) {
                result*=10;
            }
            else {
                result += q;
                result *= 10;    
            }
            
        }
        
        result /= 10;
        
        if (result == x) {
            return true;
        }
        else {
            return false;
        }
        
    }
}