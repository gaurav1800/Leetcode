class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        
        if (nums.size() < 2) {
            return nums.size();
        }
        
        sort(nums.begin(), nums.end());
        
        int n = 1;
        int result = n;
        
        for(int i = 0; i < nums.size()-1; i++) {
            if (nums[i+1] == nums[i]) {
                continue;
            }
            if (nums[i+1] - nums[i] == 1) {
                n += 1;
                result = max(result, n);
            }
            else {
                n = 1;
            }
        }
        return result;
        
    }
};