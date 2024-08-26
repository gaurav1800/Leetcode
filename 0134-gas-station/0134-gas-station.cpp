class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        
    int gasSum = accumulate(gas.begin(), gas.end(), 0);
    int costSum = accumulate(cost.begin(), cost.end(), 0);
    if (gasSum - costSum < 0)
      return -1;

    int result = 0;
    int sum = 0;
        
    int n = gas.size();

    for (int i = 0; i < n; ++i) {
      sum += gas[i] - cost[i];
      if (sum < 0) {
        sum = 0;
        result = i + 1;  // Start from next index.
      }
    }

    return result;
        
    }
};