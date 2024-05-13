class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        
        int n = nums.size();
        for(int i=0;i<n;i++){
            if(nums[abs(nums[i])] < 0){
                return abs(nums[i]);
            }
            else{
                nums[abs(nums[i])] = -nums[abs(nums[i])];
            }
        }
        return 0;
        
        
        
//         slower solution
//         set<int> my_set;
        
//         for(int num : nums) {
//             if (my_set.find(num) != my_set.end()) {
//                 return num;
//             }
//             else {
//                 my_set.insert(num);
//             }
//         }
        
//         return 0;
        
    }
};