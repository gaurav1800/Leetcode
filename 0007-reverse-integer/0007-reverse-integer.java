class Solution {
    public int reverse(int x) {
        
        if (x > -1 && x < 10 ) {
            return x;
        }
        
        if (x < Integer.MIN_VALUE || x > Integer.MAX_VALUE) {
            return 0;
        }
        
        // while (x%10 == 0) {
        //     x /= 10;
        // }
        
        boolean neg = false;
        
        if (x < 0) {
            x *= -1;
            neg = true;
        }
        
        long res = 0;
        
        while (x != 0) {
            res = res*10 + x%10;
            x/= 10;
        }
        
        if (res < Integer.MIN_VALUE || res > Integer.MAX_VALUE) {
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