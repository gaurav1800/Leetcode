class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        result = []
        deque_window = deque() 

        for i, num in enumerate(nums):
            if deque_window and deque_window[0] < i - k + 1:
                deque_window.popleft()

            while deque_window and nums[deque_window[-1]] < num:
                deque_window.pop()

            deque_window.append(i)
            if i >= k - 1:
                result.append(nums[deque_window[0]])

        return result