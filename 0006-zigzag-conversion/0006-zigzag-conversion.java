class Solution {
    public String convert(String s, int numRows) {
        if(numRows == 1){
            return s;
        }

        StringBuilder ans = new StringBuilder();
        int len = s.length();
        int sec1 = 2*(numRows -1);

        for(int i=0; i<numRows; i++){
            int index =i;
            while(index <len){
                ans.append(s.charAt(index));
                if(i != 0 && i != numRows-1){
                    int sec2 = sec1 - (2 *i);
                    int sec3 = index + sec2;

                    if(sec3 < len){
                        ans.append(s.charAt(sec3));
                    }
                }
                index = index + sec1;
            }
        }
        return ans.toString();
    }
}