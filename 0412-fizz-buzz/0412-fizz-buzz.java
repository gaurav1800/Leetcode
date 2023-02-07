class Solution {
    public List<String> fizzBuzz(int n) {
        List<String> result = new ArrayList<String>();
        
        for(int i = 0; i < n; i++) {
            if ((i+1) % 3 == 0 && (i+1) % 5 == 0) {
                result.add("FizzBuzz");
            }
            else if ((i+1) % 3 == 0 && (i+1) % 5 > 0) {
                result.add("Fizz");
            }
            else if ((i+1) % 3 > 0 && (i+1) % 5 == 0) {
                result.add("Buzz");
            }
            else {
                result.add(Integer.toString(i+1));
            }
        }
        return result;
        
    }
}