class Solution {
    public boolean isHappy(int n) {
        
        if (n == 1) {
            return true;
        }
        
        int i = 0;
        while (n > 3 && i < 100) {
            int sum = 0;
            while (n != 0) {
                sum += (n%10)*(n%10);
                n /= 10;                
            }
            if (sum == 1) {
                return true;
            }
            n = sum;
            i++;
        }
        return false;
        
    }
}