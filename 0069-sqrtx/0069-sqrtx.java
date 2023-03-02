class Solution {
    public int mySqrt(int x) {
        
        int lo=0;
        int hi=x;
        
        while (lo <= hi) {
            long mid = (lo+hi) /2;
            long sqrd = mid*mid;
            
            
            if (sqrd > x) {
                hi = (int)mid-1;
            }
            else if (sqrd < x) {
                lo = (int)mid+1;
            }
            else {
                return (int)mid;
            }
        }
        
        return hi;
        
    }
}