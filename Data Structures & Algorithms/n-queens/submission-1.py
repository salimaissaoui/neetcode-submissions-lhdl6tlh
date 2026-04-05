from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        board = [["." for _ in range(n)] for _ in range(n)]
        res = []

        def backtrack(row):
            if row == n:
                res.append(["".join(r) for r in board])
                return

            for r in range(row, row + 1):  # keep your idea of row handling
                for c in range(n):
                    check = True

                    for i in range(n):
                        # check column (only upward)
                        if r - i >= 0 and board[r - i][c] == "Q":
                            check = False
                            break
                        
                        # check top-right diagonal
                        if r - i >= 0 and c + i < n and board[r - i][c + i] == "Q":
                            check = False
                            break
                        
                        # check top-left diagonal (FIXED)
                        if r - i >= 0 and c - i >= 0 and board[r - i][c - i] == "Q":
                            check = False
                            break
                    
                    if check:
                        board[r][c] = "Q"
                        backtrack(row + 1)
                        board[r][c] = "."  # 🔑 backtrack (undo)

        backtrack(0)
        return res