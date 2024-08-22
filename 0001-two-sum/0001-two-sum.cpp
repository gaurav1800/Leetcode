class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        unordered_map<int, int> map;
        
        int n = nums.size();
        
        vector<int> result;
        
        for (int i = 0 ; i < n; i++) {
            if (map.count(target - nums[i])) {
                return {i, map[target-nums[i]]};
            }
            map[nums[i]] = i;
        }
        
        return {0};
        
        
        
        
        
    }
};