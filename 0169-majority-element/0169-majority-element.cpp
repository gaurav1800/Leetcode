class Solution {
public:
    int majorityElement(vector<int>& nums) {
        
        unordered_map<int, int> myMap;
        
        int n = nums.size();
        
        for(int num : nums) {
            myMap[num]++;
            if (myMap[num] > n/2) {
                return num;
            }
        }
        
        return 0;
        
    }
};