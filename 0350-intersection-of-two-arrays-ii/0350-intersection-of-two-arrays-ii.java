class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        
        Map<Integer, Integer> map = new HashMap<>();
        
        for(int num:nums1) {
            if (map.containsKey(num)) {
                int x = map.get(num);
                map.put(num, ++x);
            }
            else {
                map.put(num, 1);
            }
        }
        
        List<Integer> list = new ArrayList<>();
        
        for(int num:nums2) {
            if(map.containsKey(num)) {
                int x = map.get(num);
                if (x > 0) {
                    list.add(num);
                    map.put(num, --x);
                }
            }
        }
        
        int[] res = new int[list.size()];
        for(int i = 0; i < list.size(); i++) {
            res[i] = list.get(i);
        }
        
        return res;
        
        
        
        
        
        
    }
}