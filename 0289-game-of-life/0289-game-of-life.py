class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                ones = 0
                for a in range(max(0, i-1), min(m, i+2)):
                    for b in range(max(0, j-1), min(n, j+2)):
                        ones += board[a][b] & 1
                # cell with 2 or 3 live neighbors living onto the next gen
                if board[i][j] == 1 and (ones == 3 or ones == 4):
                    board[i][j] |= 0b10
                
                # dead cell with exactly 3 alive neighbors becomes alive
                if board[i][j] == 0 and ones == 3:
                    board[i][j] |= 0b10
        
        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1

        