class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen = set()
            for val in row:
                if val != ".":
                    if val in seen:
                        return False
                    seen.add(val)
        
        transposed = list(zip(*board))

        for row in transposed:
            seen = set()
            for val in row:
                if val != ".":
                    if val in seen:
                        return False
                    seen.add(val)

        
        squares = []
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                square = []

                for r in range(box_row, box_row + 3):
                    for c in range(box_col, box_col + 3):
                        square.append(board[r][c])
                squares.append(square)

        for row in squares:
            seen = set()
            for val in row:
                if val != ".":
                    if val in seen:
                        return False
                    seen.add(val)
        
        return True