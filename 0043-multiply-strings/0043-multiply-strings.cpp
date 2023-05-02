class Solution {
public:
    string multiply(string num1, string num2) {
        
        string a(num1.length() + num2.length(), '0');
        
        for(int i=num1.length()-1; i >= 0; i--) {
            for(int j=num2.length()-1; j >= 0; j--) {
                int mult = (num1[i] - '0') * (num2[j] - '0');
                int sum = mult + (a[i+j+1] - '0');
                a[i+j] += sum/10;
                a[i+j+1] = '0' + sum%10;
            }
        }
        
        int i = a.find_first_not_of('0');
        return i == -1 ? "0" : a.substr(i);
        
    }
};