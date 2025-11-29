class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        
        h = [1, 2, 4, 8]
        m = [1, 2, 4, 8, 16, 32]

        result = []

        def dfs(turnedOn, start, hours, minutes):
            if turnedOn == 0:
                time = str(hours) + ":" + (str(minutes).zfill(2))
                result.append(time)
                return
            
            for i in range(start, len(h) + len(m)):
                if i < 4 and hours + h[i] < 12:
                    dfs(turnedOn-1, i+1, hours + h[i], minutes)
                elif i >= 4 and minutes + m[i-4] < 60:
                    dfs(turnedOn-1, i+1, hours, minutes + m[i-4])
        
        dfs(turnedOn, 0, 0, 0)
        return result