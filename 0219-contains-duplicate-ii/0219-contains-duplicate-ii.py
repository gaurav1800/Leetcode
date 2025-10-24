class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        seen = {}
        for i, n in enumerate(nums):
            if n in seen and abs(seen[n] - i) <= k: return True
            else: seen[n] = i
        
        return False
        
        # slow solution
        # if len(nums) < k:
        #     return len(set(nums)) != len(nums)
        # queue = deque()
        # seen = set()

        # for n in nums:
        #     if len(queue) != k+1:
        #         queue.append(n)
        #         seen.add(n)
        #     else:
        #         temp = queue.popleft()
        #         seen.remove(temp)
        #         queue.append(n)
        #         seen.add(n)

        #     if len(queue) != len(seen):
        #         return True
        # return False