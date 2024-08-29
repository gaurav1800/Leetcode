class Solution {
public:
    int reverse(int x) {
        long result = 0;
        
        long y = x;
        
        int flag = 0;
        
        if (y < 0) {
            flag = 1;
            y *= -1;
        }
        
        while (y != 0) {
            int temp = y%10;
            result += temp;
            
            if (result > INT_MAX || result < INT_MIN) {
                return 0;
            }
            
            result *= 10;
            y /= 10;
            
        }
        
        result /= 10;
        
        if (flag == 1) {
            result *= -1;
        }
        
        if (result > INT_MAX || result < INT_MIN) {
                return 0;
        }
        
        
        return result;
        
    }
};