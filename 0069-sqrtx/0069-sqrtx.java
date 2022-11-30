class Solution {
    public int mySqrt(int x) {
        
        
        if(x == 0 || x == 1) {
            return x;
        }
        else if(x == 2 || x == 3) {
            return 1;
        }
        else {
            for(long i = 2; i <= x/2; i++) {
                // if (i*i == x) {
                //     return i;
                // }
                if ((i+1)*(i+1) > x) {
                    return (int)i;
                }
            }
        }
        
        return 0;
    }
}