/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        long lo=1, hi=n;
        
        while (lo<hi) {
            long mid = (lo+hi)/2;
            if (isBadVersion((int)mid) == true && isBadVersion((int)mid-1) == false) {
                return (int) mid;
            }
            else if (isBadVersion((int)mid) == false) {
                lo = mid+1;
            }
            else{
                hi = mid-1;
            }
        }
        if (isBadVersion((int)lo) == true) {
            return (int) lo;
        }
        else {
            return (int)hi;
        }
        
    }
}