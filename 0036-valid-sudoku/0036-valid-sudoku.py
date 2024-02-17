class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # for i in range(9):
        #     for j in range(1, 10):
        #         if j not in board[i]:
        #             return False
        #     for j in range(9):
        #         if
        
        seen = set()
        for i in range(9):
            for j in range(9):
                current_val = board[i][j]
                if current_val != '.':
                    # Check for the same value in the current row
                    if (i, current_val) in seen:
                        return False
                    seen.add((i, current_val))

                    # Check for the same value in the current column
                    if (current_val, j) in seen:
                        return False
                    seen.add((current_val, j))

                    # Check for the same value in the current 3x3 subgrid
                    if (i // 3, j // 3, current_val) in seen:
                        return False
                    seen.add((i // 3, j // 3, current_val))

        return True
                
        