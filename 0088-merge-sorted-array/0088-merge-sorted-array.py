class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1ptr = m-1
        nums2ptr = n-1
        
        for i in range(m+n-1, -1, -1):
            if nums1ptr > -1 and nums2ptr > -1:
                if nums1[nums1ptr] < nums2[nums2ptr]:
                    nums1[i] = nums2[nums2ptr]
                    nums2ptr -= 1
                elif nums1[nums1ptr] >= nums2[nums2ptr]:
                    nums1[i] = nums1[nums1ptr]
                    nums1ptr -= 1
            else:
                if nums1ptr > -1:
                    nums1[i] = nums1[nums1ptr]
                    nums1ptr -= 1
                else:
                    nums1[i] = nums2[nums2ptr]
                    nums2ptr -= 1
        
            