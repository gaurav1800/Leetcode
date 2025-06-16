class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        # fast solution
        seen = {}
        for i, num in enumerate(nums):
            if num in seen and abs(seen[num]-i) <= k:
                return True
            else:
                seen[num] = i

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





