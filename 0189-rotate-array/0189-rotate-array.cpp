#include <bits/stdc++.h>

class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        
        k %= nums.size();
        
        int n = nums.size();
        
        reverse(nums, 0, n - 1);
        reverse(nums, 0, k - 1);
        reverse(nums, k, n - 1);
        
    
        
        
    }
    
    
    
    void reverse(vector<int>& nums, int left, int right) {
        while (left < right) {
            swap(nums[left], nums[right]);
            left++;
            right--;
        }
    }
};