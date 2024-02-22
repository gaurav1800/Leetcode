class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
#         result = []
        
#         for i in nums:
#             for j in nums[1:]:
#                 for k in nums[2:]:
#                     if i + j + k == 0:
#                         result.append([i, j, k])
        
#         mySet = set(result)
#         return list(mySet)

        result = []
        nums.sort()  # Sort the array to simplify the solution

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicate elements to avoid duplicate triplets

            left, right = i + 1, len(nums) - 1

            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]

                if curr_sum < 0:
                    left += 1
                elif curr_sum > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1  # Skip duplicate elements
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1  # Skip duplicate elements
                    left += 1
                    right -= 1

        return result