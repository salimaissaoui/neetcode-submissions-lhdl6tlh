from typing import List
from collections import defaultdict

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        adjacency = defaultdict(list)
        rotten = set()
        fresh = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    continue
                if grid[r][c] == 2:
                    rotten.add((r, c))
                else:
                    fresh.add((r, c))
                for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != 0:
                        adjacency[(r, c)].append((nr, nc))

        if not fresh:
            return 0

        minutes = 0
        while fresh:
            newly_rotten = set()
            for pos in rotten:
                for neighbor in adjacency[pos]:
                    if neighbor in fresh:
                        newly_rotten.add(neighbor)
            if not newly_rotten:
                return -1
            fresh -= newly_rotten
            rotten = newly_rotten
            minutes += 1

        return minutes
