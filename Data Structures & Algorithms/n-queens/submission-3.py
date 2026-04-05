from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        board = [["." for _ in range(n)] for _ in range(n)]
        res = []

        cols = set()
        diag1 = set()
        diag2 = set()

        def backtrack(row):
            if row == n:
                res.append(["".join(r) for r in board])
                return

            placed = False

            for r in range(row, row + 1):  # keep your structure
                for c in range(n):
                    
                    # 🔑 O(1) checks instead of loop
                    if c in cols or (r - c) in diag1 or (r + c) in diag2:
                        continue

                    placed = True

                    # place
                    board[r][c] = "Q"
                    cols.add(c)
                    diag1.add(r - c)
                    diag2.add(r + c)

                    backtrack(row + 1)

                    # 🔑 undo (backtrack)
                    board[r][c] = "."
                    cols.remove(c)
                    diag1.remove(r - c)
                    diag2.remove(r + c)

            if not placed:
                return

        backtrack(0)
        return res