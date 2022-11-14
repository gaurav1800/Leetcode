import java.util.*;

class Solution {
    public int romanToInt(String s) {
        char[] arr = s.toCharArray();
        
        int i = 0, sum = 0;
        
        while (i != arr.length) {
            
            if ((arr[i] == 'M' && i+1== arr.length) || (arr[i] == 'M' && arr[i+1] == 'M') || arr[i] == 'M') {
                sum += 1000;
            }
            else if (arr[i] == 'C' && i+1 != arr.length && arr[i+1] == 'M') {
                sum += 900;
                i++;
            }
            else if ((arr[i] == 'D' && i+1== arr.length) || (arr[i] == 'D' && arr[i+1] == 'D') || arr[i] == 'D') {
                sum += 500;
            }
            else if (arr[i] == 'C' && i+1 != arr.length && arr[i+1] == 'D') {
                sum += 400;
                i++;
            }
            else if ((arr[i] == 'C' && i+1 == arr.length) || (arr[i] == 'C' && arr[i+1] == 'C') || arr[i] == 'C') {
                sum += 100;
            }
            else if (arr[i] == 'X' && i+1 != arr.length && arr[i+1] == 'C') {
                sum += 90;
                i++;
            }
            else if ((arr[i] == 'L' && i+1== arr.length) || (arr[i] == 'L' && arr[i+1] == 'L') || arr[i] == 'L') {
                sum += 50;
            }
            else if ((arr[i] == 'X' && i+1 != arr.length) && arr[i+1] == 'L') {
                sum += 40;
                i++;
            }
            else if ((arr[i] == 'X' && i+1== arr.length) || (arr[i] == 'X' && arr[i+1] == 'X') || arr[i] == 'X') {
                sum += 10;
            } 
            else if (arr[i] == 'I' && i+1 != arr.length && arr[i+1] == 'X') {
                sum += 9;
                i++;
            }
            else if ((arr[i] == 'V' && i+1== arr.length) || (arr[i] == 'V' && arr[i+1] == 'V') || arr[i] == 'V') {
                sum += 5;
            }
            else if (arr[i] == 'I' && i+1 != arr.length && arr[i+1] == 'V') {
                sum += 4;
                i++;
            }
            else if ((arr[i] == 'I' && i+1== arr.length) || (arr[i] == 'I' && arr[i+1] == 'I')) {
                sum += 1;
            }
            
               
            i++;
        }
        return sum;
        
    }
}