class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        queue = collections.deque()

        rows, cols = len(grid), len(grid[0])
        
        
        def bfs(grid, queue):

            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            while queue:
                r,c = queue.popleft()
                for dr, dc in directions:
                    if 0 <= r + dr < rows and 0 <= c+ dc < cols and grid[r + dr][c + dc] == "1":
                        queue.append((r + dr, c + dc))
                        grid[r + dr][c + dc] = "0"
                
            return 
       

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    queue.append((r,c))
                    bfs(grid, queue)
                    count +=1
                    
        return count


                    
                    
            

       




        