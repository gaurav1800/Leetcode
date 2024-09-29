class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        
        intervals.sort(key = lambda x: x[0])
        
        heap = []
        
        for i in range(len(intervals)):
            start, end = intervals[i]
            
            if heap and heap[0] <= start:
                heappop(heap)
            
            heappush(heap, end)
        
        return len(heap)
        
        
        
#         # longer solution
#         if len(intervals) == 1:
#             return 1
        
#         intervals.sort(key = lambda x: x[0])
        
#         rooms = [intervals[0]]
#         total = 1
        
        
#         for i in range(1, len(intervals)):
#             j = 0
#             while j < len(rooms):
#                 if rooms[j][1] <= intervals[i][0]:
#                     rooms[j] = intervals[i]
#                     break
#                 else:
#                     j+=1
#             if j == len(rooms):
#                 rooms.append(intervals[i])
                
#         return len(rooms)