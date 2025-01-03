class Solution {
public:
    int climbStairs(int n) {
        
        if (n <= 3) {
            return n;
        }
        
        int first = 2;
        int second = 3;
        int result = 0;
        
        for(int i = 4; i <= n; i++) {
            result = first + second;
            first = second;
            second = result;
        }
        
        return result;
        
        
        
        
        
        
        
        // using DP approach
//         int* arr= new int[n+1];
        
//         arr[1] = 1;
//         arr[2] = 2;
//         arr[3] = 3;
        
//         for(int i = 4; i <= n; i++) {
//             arr[i] = arr[i-1] + arr[i-2];
//         }
        
//         int result = arr[n];
        
//         delete[] arr;
        
//         return result;
        
    }
};