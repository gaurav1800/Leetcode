class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        result = []
        maximum = deque()

        for i, num in enumerate(nums):
            while maximum and maximum[-1] < num:
                maximum.pop()

            maximum.append(num)

            if i >= k and nums[i - k] == maximum[0]:  # out-of-bounds
                maximum.popleft()

            if i >= k - 1:
                result.append(maximum[0])

        return result