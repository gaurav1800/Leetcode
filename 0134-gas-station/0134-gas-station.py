class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        result = 0
        difference = 0
        total = 0

        for i in range(len(gas)):
            difference += gas[i] - cost[i]
            total += gas[i] - cost[i]
            if total < 0:
                total = 0
                result = i + 1  # Start from next i

        return -1 if difference < 0 else result