class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        queue = [-stone for stone in stones]
        heapq.heapify(queue)

        while len(queue) >= 2:
            first = -heapq.heappop(queue)
            second = -heapq.heappop(queue)
            if first != second:
                heapq.heappush(queue, -(first - second))

        if queue:
            return -queue[0]
        return 0