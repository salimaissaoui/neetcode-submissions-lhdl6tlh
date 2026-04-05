from typing import List
import collections

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid or not grid[0]:
            return  # Edge case: Empty grid

        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = collections.deque()

        # Step 1: Find all the treasure locations (0s) and add to queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:  # Treasure location
                    queue.append((r, c))

        # Step 2: Perform BFS from all treasures
        while queue:
            r, c = queue.popleft()  # Get current cell
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check bounds and update only ocean cells (2147483647)
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 2147483647:
                    grid[nr][nc] = grid[r][c] + 1  # Update distance
                    queue.append((nr, nc))  # Add to queue for further processing
