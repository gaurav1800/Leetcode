class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        
        if (nums.size() <= 1) {
            return nums.size();    
        }
        
        
        // converting the vector to a set
        set<int> mySet;
        
        for(int i : nums) {
            mySet.insert(i);
        }
        
        int length = 1;
        int longest = 0;
        
        for(int i : mySet) {
            if (mySet.find(i-1) == mySet.end()) {
                length = 1;
                
                while(mySet.find(i+length) != mySet.end()) {
                    length++;
                }
            }
            longest = max(length, longest);
        }
        
        return longest;
        
    }
};