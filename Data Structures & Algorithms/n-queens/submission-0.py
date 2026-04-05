from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        board = [["." for _ in range(n)] for _ in range(n)]
        res = []

        def backtrack(row):
            if row == n:
                res.append(["".join(r) for r in board])
                return

            placed = False  # track if this row found a valid spot

            for r in range(row, row + 1):  # keep your structure
                for c in range(n):
                    check = True

                    for i in range(n):
                        # check column
                        if r - i >= 0 and board[r - i][c] == "Q":
                            check = False
                            break
                        
                        # check top-right diagonal
                        if r - i >= 0 and c + i < n and board[r - i][c + i] == "Q":
                            check = False
                            break
                        
                        # check top-left diagonal
                        if r - i >= 0 and c - i >= 0 and board[r - i][c - i] == "Q":
                            check = False
                            break
                    
                    if check:
                        placed = True
                        board[r][c] = "Q"
                        
                        backtrack(row + 1)  # go forward
                        
                        board[r][c] = "."   # 🔑 undo (so we can try others)

            if not placed:
                return  # 🔑 nothing worked → go back (your idea)

        backtrack(0)
        return res