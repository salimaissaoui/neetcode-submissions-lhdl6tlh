class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0

        rows,cols = len(grid), len(grid[0])


        def bfs(grid,r ,c):
            queue = deque([(r,c)])
            area = 1
            directions = [(0,1), (0,-1), (1,0), (-1,0)]
            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    if  0<= r + dr < rows and 0 <= c + dc < cols and  grid[r + dr][c + dc] == 1:
                        grid[r+dr][c+dc] = 0
                        queue.append((r + dr, c + dc))
                        area+=1
                        
                   
            return area


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    grid[r][c] = 0
                    max_area = max(max_area, bfs(grid, r, c))
        return max_area

        