/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        int lo=0, hi=n;
        
        while (lo<hi) {
            int mid = (hi-lo)/2+lo;
            boolean isBad = isBadVersion(mid);
            // if (isBad && !isBadVersion(mid-1)) {
            //     return mid;
            // }
            // else if (!isBad) {
            //     lo = mid+1;
            // }
            // else{
            //     hi = mid-1;
            // }
            if (!isBad) {
                lo = mid+1;
            }
            else{
                hi = mid;
            }
        }
        return lo;
        
    }
}