class Solution {
    public int[] plusOne(int[] digits) {
        
        int i = 0, counter = 0;
        while(i < digits.length) {
            if (digits[i] == 9) {
                counter += 1;
            }
            i++;
        }
        
        
        if (digits.length == counter) {
            int[] result = new int[digits.length+1];
            for(i=0; i<digits.length; i++) {
                result[i+1] = digits[i];
            }
            
            int num = result.length-1;
            
            while (result[num] == 9) {
                result[num] = 0;
                num--;
            }
            result[num] += 1;
            
            return result;
            
        }
        else if (counter < digits.length) {
            int num = digits.length - 1;
            
            while (digits[num] == 9) {
                digits[num] = 0;
                num--;
            }
            digits[num] += 1;
            return digits;
        }
        else {
            digits[digits.length-1] = digits[digits.length-1]+1;
            return digits;
        }
        
        
        
        
        
        
    }
}