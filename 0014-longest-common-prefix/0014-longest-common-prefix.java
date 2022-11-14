class Solution {
    public String longestCommonPrefix(String[] strs) {
        
        char[] word = strs[0].toCharArray();
        int size = word.length;
        
        int i = 1;
        
        while (i != strs.length) {
            char[] secWord = strs[i].toCharArray();
            int j = 0;
            if (secWord.length < size){
                size=secWord.length;
            } 
            
            while (j != size && word[j] == secWord[j]) {
                
                j++;
            }
            if (j < size) {
                size=j;
            } 
            
            i++;
        }
        
        if (size == 0) {
            return "";
        }
        else {
            String result = "";
            for (int k=0; k<size; k++) {
                result += word[k];
            }
            return result;
        }
    }
}