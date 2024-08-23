class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        
        unordered_map<int, int> myMap;
        
        int counter = nums.size();
        
        for(int n : nums) {
            if (myMap.find(n) == myMap.end()) {
                myMap[n] = 1;
            }
            else {
                myMap[n]++;
            }
        }
        
        for (int i = 0; i < nums.size(); i++) {
            if (myMap[nums[i]] > 2) {
                myMap[nums[i]]--;
                counter--;
                nums[i] = INT_MIN;
            }
        }
        
        int i = 0;
        
        while (i < nums.size()) {
            int j = i + 1;
            if (nums[i] == INT_MIN) {
                while (j < nums.size() && nums[j] == INT_MIN) {
                    j++;
                }
                if (j == nums.size()) {
                    break;
                }
                swap(nums[i], nums[j]);    
            }
            if (j == nums.size()) {
                    break;
                }
            i++;
        }
        
        return counter;
        
    }
};