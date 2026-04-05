from typing import List
from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        def bfs(starts):
            res = set()
            queue = deque(starts)

            while queue:
                r, c = queue.popleft()
                res.add((r, c))
                directions = [(1,0), (0,1), (-1,0), (0,-1)]

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < len(heights) and 0 <= nc < len(heights[0]):
                        if heights[nr][nc] >= heights[r][c] and (nr,nc) not in res:
                            queue.append((nr, nc))
            return res
        
        m, n = len(heights), len(heights[0])

        # Start BFS from all Pacific border cells
        pacific_starts = [(0, c) for c in range(n)] + [(r, 0) for r in range(m)]
        atlantic_starts = [(m-1, c) for c in range(n)] + [(r, n-1) for r in range(m)]

        pacific = bfs(pacific_starts)
        atlantic = bfs(atlantic_starts)

        return list(pacific & atlantic)