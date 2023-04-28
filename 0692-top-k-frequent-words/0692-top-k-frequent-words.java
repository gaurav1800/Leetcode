class T {
    public String word;
    public int freq;
    public T(String word, int freq) {
        this.word = word;
        this.freq = freq;
    }
}


class Solution {
    public List<String> topKFrequent(String[] words, int k) {
        
        List<String> ans = new ArrayList<>();
        
        Map<String, Integer> map = new HashMap();
        
        Queue<T> heap = new PriorityQueue<>(
            (a, b) -> a.freq == b.freq ? b.word.compareTo(a.word) : a.freq - b.freq);
        
        for (String word : words) {
            map.merge(word, 1, Integer :: sum);
        }
        
        for(String word : map.keySet()) {
            heap.offer(new T(word, map.get(word)));
            if (heap.size() > k) {
                heap.poll();
            }
        }
        
        while (!heap.isEmpty()) {
            ans.add(heap.poll().word);
        }
        
        Collections.reverse(ans);
        return ans;
        
        
    }
}