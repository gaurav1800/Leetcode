class Solution {
    public int reverse(int x) {
        
        if (x > -1 && x < 10 ) {
            return x;
        }
        
        if (x < Math.pow(-2, 31) || x > (Math.pow(2, 31) - 1)) {
            return 0;
        }
        
        while (x%10 == 0) {
            x /= 10;
        }
        
        boolean neg = false;
        
        if (x < 0) {
            x *= -1;
            neg = true;
        }
        
        long res = 0;
        
        while (x != 0) {
            int rem = x%10;
            res += rem;
            res *= 10;
            x/= 10;
        }
        res /= 10;
        
        if (res < Math.pow(-2, 31) || res > (Math.pow(2, 31) - 1)) {
            return 0;
        }
        if (neg == true) {
            return (int)res*-1;
        }
        else {
            return (int)res;
        }
        
    }
}