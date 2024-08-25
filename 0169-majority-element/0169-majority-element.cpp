class Solution {
public:
    int majorityElement(vector<int>& nums) {
        
        int counter = 0;
        
        int maxn = 0;

        for(int num : nums){
            if(counter == 0){
                maxn = num;
            }
            
            if(num == maxn){
                counter++;
            }
            else {
                counter--;
            }

        }
        return maxn;
        
        
        
        // inefficient
//         unordered_map<int, int> myMap;
        
//         int n = nums.size();
        
//         for(int num : nums) {
//             myMap[num]++;
//             if (myMap[num] > n/2) {
//                 return num;
//             }
//         }
        
//         return 0;
        
    }
};