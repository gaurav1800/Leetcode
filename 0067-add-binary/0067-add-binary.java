class Solution {
    public String addBinary(String a, String b) {
        
        char[] aArr = a.toCharArray();
        char[] bArr = b.toCharArray();
        
        boolean carry;
        
        int size = aArr.length >= bArr.length ? aArr.length : bArr.length;
        
        char[] res = new char[size+1];
        
        for(int i = 0; i < size+1; i++) {
            res[i] = '0';
        }
        
        int i = aArr.length-1, j = bArr.length-1, k = size;
        carry = false;
            
        
        while (i >= 0 || j >= 0) {
            
            if (carry == true) {
                if (i < 0) {
                    if (bArr[j] == '0') {
                        res[k] = '1';
                        carry = false;    
                    }
                    else if (bArr[j] == '1') {
                        res[k] = '0';
                        carry = true;
                    }
                }
                
                else if (j < 0) {
                    if (aArr[i] == '0') {
                        res[k] = '1';
                        carry = false;                        
                    }
                    else if (aArr[i] == '1') {
                        res[k] = '0';
                        carry = true;
                    }
                }
                else if ((bArr[j] == '0' && aArr[i] == '1') || (bArr[j] == '1' && aArr[i] == '0')){
                    res[k] = '0';
                    carry = true;
                }
                else if (bArr[j] == '0' && aArr[i] == '0') {
                    res[k] = '1';
                    carry = false;
                }
                else {
                    res[k] = '1';
                    carry = true;
                }
            }
            else {
                if (i < 0) {
                    res[k] = bArr[j];
                }
                else if (j < 0) {
                    res[k] = aArr[i];
                }
                else {
                    if ((aArr[i] == '0' && bArr[j] == '1') || (aArr[i] == '1' && bArr[j] == '0')) {
                        res[k] = '1';
                    }
                    else if ((aArr[i] == '0' && bArr[j] == '0')) {
                        res[k] = '0';
                    }
                    else {
                        res[k] = '0';
                        carry = true;
                    }
                    
                }
            }
            
            i--;
            j--;
            k--;
        }
        String result;
        if (carry == true) {
            res[k] = '1';
            result = String.valueOf(res);
        }
        else {
            // for(int z = 0; z < size; i++) {
            //         res[z] = res[z+1];
            // }
            result = String.valueOf(res);
            result = result.substring(1);
        }
            
        // String result = String.valueOf(res);    
        return result;
        
    }
}