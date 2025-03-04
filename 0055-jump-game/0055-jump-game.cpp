class Solution {
public:
    bool canJump(vector<int>& nums) {

        int last = nums.size() - 1;
        
        for(int i = nums.size() - 2; 0 <= i; i--) {
            if (i + nums[i] >= last) {
                last = i;
            }
        }
        return last == 0;
        
    }
};