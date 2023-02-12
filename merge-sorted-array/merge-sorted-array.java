class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        
        
        if(m+n == 1) {
            if (m == 1) {
                nums1[0] = nums1[0];
            }
            else if(n == 1) {
                nums1[0] = nums2[0];
            }
            
        }
        else {
            int k = m+n-1;
            m--;
            n--;

            while(k>0 && m>-1 && n>-1) {
                if (nums1[m] >= nums2[n]) {
                    nums1[k] = nums1[m];
                    m--;
                }
                else {
                    nums1[k] = nums2[n];
                    n--;
                }
                k--;
            }

            while (n > -1 && m < 0) {
                nums1[k] = nums2[n];
                n--;
                k--;
            }
            // while (m > -1 && n < 0) {
            //     nums1[k] = nums2[n];
            // }
            
            
        }
        
        
        
        
    
        
        
//         int[] res = new int[m+n];
        
//         int i = 0, j = 0, k = 0;
        
//         if (nums2.length != 0) {
//             while (k != m+n) {
//                 if (j == n) {
//                     res[k] = nums1[i];
//                     i++;
//                 }
//                 else if (nums1[i] <= nums2[j] && i != m) {
//                     res[k] = nums1[i];
//                     i++;
//                 } 
//                 else {
//                     res[k] = nums2[j];
//                     j++;
//                 }
//             k++;
//         }
        
//             for(int z = 0; z < m+n; z++) {
//                 nums1[z] = res[z];
//             }    
//         }
        
        
        
        
        
        
        
    }
}