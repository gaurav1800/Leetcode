class Solution {
    public boolean isPalindrome(int x) {
        
        if (x<0) {
            return false;
        }
        
        int num = 0;
        int x1 = x;
        
        while (x>0) {
            num = num*10 + x%10;
            x /= 10;
        }
        
        return num == x1;
        
        
        
        //converting int to string first approach
//         String num = String.valueOf(x);
        
//         int i=0, j=num.length()-1;
        
//         while (i<j) {
//             if (num.charAt(i) != num.charAt(j)) {
//                 return false;
//             }
//             i++;
//             j--;
//         }
//         return true;
        
    }
}
