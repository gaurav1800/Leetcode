class Solution {
public:
    int candy(vector<int>& ratings) {
        
        int n = ratings.size();
        
        vector<int> fromLeft(n);
        vector<int> fromRight(n);
        
        int counter = n;
        
        for (int i = 1; i < n; i++) {
            if (ratings[i] > ratings[i-1]) {
                fromLeft[i] = fromLeft[i-1] + 1; 
            }
        }
        for (int i = n-2; i >= 0; i--) {
            if (ratings[i] > ratings[i+1]) {
                fromRight[i] = fromRight[i+1] + 1;
            }
        }
        
        for (int i = 0; i < n; i++) {
            counter += max(fromLeft[i], fromRight[i]);
        }
        return counter;
        
    }
};