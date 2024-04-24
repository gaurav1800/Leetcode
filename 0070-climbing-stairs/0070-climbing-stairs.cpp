class Solution {
public:
    int climbStairs(int n) {
        
        if (n <= 3) {
            return n;
        }
        
        int first = 2;
        int second = 3;
        
        for (int i = 3; i<n; i++) {
            int temp = first + second;
            first = second;
            second = temp;
        }
        
        return second;
    }
};