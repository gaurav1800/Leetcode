class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        
        // much more efficient solution
        int n = nums.size();
        
        if (n < 3) {
            return n;
        }
        
        int x = 2;
        
        
        for(int y = 2; y < n; y++) {
            if (nums[y] != nums[x-2]) {
                nums[x] = nums[y];
                x++;
            }
        }
        
        return x;
        
        
        
        
        // longer and more complex solution
//         unordered_map<int, int> myMap;
        
//         int counter = nums.size();
        
//         for(int num : nums) {
//             if (myMap.find(num) == myMap.end()) {
//                 myMap[num] = 1;
//             }
//             else {
//                 myMap[num]++;
//             }
//         }
        
//         for (int i = 0; i < nums.size(); i++) {
//             if (myMap[nums[i]] > 2) {
//                 myMap[nums[i]]--;
//                 counter--;
//                 nums[i] = INT_MIN;
//             }
//         }
        
//         int i = 0;
        
//         while (i < nums.size()) {
//             int j = i + 1;
//             if (nums[i] == INT_MIN) {
//                 while (j < nums.size() && nums[j] == INT_MIN) {
//                     j++;
//                 }
//                 if (j == nums.size()) {
//                     break;
//                 }
//                 swap(nums[i], nums[j]);    
//             }
//             if (j == nums.size()) {
//                     break;
//                 }
//             i++;
//         }
        
//         return counter;
        
    }
};