class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        
        int[] res = new int[m+n];
        
        int i = 0, j = 0, k = 0;
        
        if (nums2.length != 0) {
            while (k != m+n) {
                if (j == n) {
                    res[k] = nums1[i];
                    i++;
                }
                else if (nums1[i] <= nums2[j] && i != m) {
                    res[k] = nums1[i];
                    i++;
                } 
                else {
                    res[k] = nums2[j];
                    j++;
                }
            k++;
        }
        
            for(int z = 0; z < m+n; z++) {
                nums1[z] = res[z];
            }    
        }
        
        
        
        
        
        
//         int i = 0, j = 0;
        
//         while (i < m+n && j < n) {
//             if (nums1[i] <= nums2[j]) {
//                 i++;
//             }
//             else if (nums1[i] > nums2[j]) {
//                 while () {
                    
//                 }
//                 int k = i
                
//                 j++;
//             }
//         }
        
    }
}