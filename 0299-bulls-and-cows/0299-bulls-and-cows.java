class Solution {
    public String getHint(String secret, String guess) {
        
        int bulls = 0, cows = 0;
        
        char[] sec = secret.toCharArray();
        
        
        HashMap<Integer, Character> map = new HashMap<>();
        for(int i=0; i<guess.length(); i++) {
            map.put(i, guess.charAt(i));
        }
        
        for(int i=0; i<sec.length; i++) {
            if (sec[i] == map.get(i)) {
                bulls++;
                map.remove(i);
                sec[i] = 'a';
            }
        }
        
        for(int i=0; i<sec.length; i++) {
            if (map.containsValue(sec[i])) {
                cows++;
                char value = sec[i];
                int j = 0;
                while (true) {
                    if (!map.containsKey(j)) {
                        j++;
                    }
                    else {
                        if (value == map.get(j)) {
                            map.remove(j);
                            break;
                        }
                        j++;
                    }
                }
            }
        }
        String result = String.valueOf(bulls) + 'A' + String.valueOf(cows) + 'B';
        return result;
        
    }
}