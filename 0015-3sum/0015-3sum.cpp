class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        
        vector<vector<int>> result;
        
        int n = nums.size();
        
        if (n < 3) {
            return result;
        }
        
        sort(nums.begin(), nums.end());
        
        for(int i=0; i<n-2; i++) {
            if (nums[i] > 0) {
                break;
            }
            
            if (i > 0 && nums[i] == nums[i-1]) {
                continue;
            }
            
            int j = i + 1;
            int k = n - 1;
            
            while(j<k) {
                if (nums[i] + nums[j] + nums[k] < 0) {
                    j++;
                }
                else if (nums[i] + nums[j] + nums[k] > 0) {
                    k--;
                }
                else {
                    result.push_back({nums[i], nums[j], nums[k]});
                    
                    while (j < k && nums[j] == nums[j+1]) {
                        j++;
                    }
                    j++;
                    while(j<k && nums[k] == nums[k-1]) {
                        k--;
                    }
                    k--;
                }
                
            }
        }
        
        return result;
        
        
    }
};