class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        
        set<int> my_set;
        
        for(int num : nums) {
            if (my_set.find(num) != my_set.end()) {
                return num;
            }
            else {
                my_set.insert(num);
            }
        }
        
        return 0;
        
    }
};