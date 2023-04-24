class Solution {
    public int lastStoneWeight(int[] stones) {
        
        
        
        Arrays.sort(stones);
        
        for(int i=stones.length-1; i>=0; i--) {
            if (i-1 == -1) {
                return stones[i];
            }
            else if (stones[i] - stones[i-1] == 0) {
                i--;
            }
            else {
                int diff = stones[i] - stones[i-1];
                stones[i-1] = diff;
                Arrays.sort(stones);
            }
        }
        return 0;
        
    }
}