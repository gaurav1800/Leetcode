/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        
        int lo=1, hi=n;
        
        while(lo < hi) {
            int mid = (hi-lo)/2 + lo;
            
            boolean bad = isBadVersion(mid);
            
            if (!bad) {
                lo = mid+1;
            }
            else {
                hi = mid;
            }
        }
        return lo;
        
    }
}