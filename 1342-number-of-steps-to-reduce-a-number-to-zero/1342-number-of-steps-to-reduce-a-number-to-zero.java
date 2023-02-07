class Solution {
    
    int counter = 0;
    
    public int numberOfSteps(int num) {
        
        if (num == 0) {
            return counter;
        }
        
        if(num%2 == 0) {
            num /= 2;
        }
        else {
            num--;
        }
        counter++;
        return numberOfSteps(num);
        
    }
}