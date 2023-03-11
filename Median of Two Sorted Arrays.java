class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
   
        
        int[] arr = new int[nums1.length+nums2.length];
        
        int i=0, j=0, k=0;
        while (i!=nums1.length || j!=nums2.length) {
            if (i==nums1.length) {
                arr[k] = nums2[j];
                j++;
                k++;
            }
            else if (j==nums2.length) {
                arr[k] = nums1[i];
                i++;
                k++;
            }
            else if (nums1[i]<nums2[j]) {
                arr[k]=nums1[i];
                i++;
                k++;
            }
            else {
                arr[k]=nums2[j];
                j++;
                k++;
            }
            
        }
        if (k%2 == 1) {
            return arr[k/2];
        }
        else {
            return (((double)arr[k/2 - 1]+(double)arr[k/2])/2);
        }
    }
}
