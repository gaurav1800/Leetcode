class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        
        if (nums1.length > nums2.length) {
            return intersect(nums2,nums1);
        }
        
        List<Integer> list = new ArrayList<>();
        Map<Integer, Integer> counter = new HashMap<>();
        
        for(int num : nums1) {
            counter.put(num, counter.getOrDefault(num,0) + 1);
        }
        
        for(int num : nums2) {
            if (counter.containsKey(num) && counter.get(num) > 0) {
                list.add(num);
                counter.put(num, counter.get(num) - 1);
            }
        }
        
        return list.stream().mapToInt(Integer::intValue).toArray();
        
    }
}