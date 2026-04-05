class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """pseudocode logic

            for r in grid:
                for c in grid:
                    if grid[r][c] == 1 and (r,c) not in visited:
                        visited.add((r,c)) 
                        queue.add((r,c)) ( all directions)
                        while queue:

        """


        visited = set()
        res = 0
        queue = deque()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r,c) not in visited:
                        visited.add((r,c)) 
                        queue.append((r+1, c))
                        queue.append((r, c+1))
                        queue.append((r-1, c))
                        queue.append((r, c-1))
                        res += 1
                        while queue:
                            node = queue.popleft()
                            print(node)
                            if node[0] < len(grid) and node[1] < len(grid[0]) and node[0] >= 0 and node[1] >= 0 and grid[node[0]][node[1]] == "1" and (node[0], node[1]) not in visited:
                                visited.add((node[0], node[1]))
                                queue.append((node[0]+1, node[1]))
                                queue.append((node[0], node[1]+1))
                                queue.append((node[0]-1, node[1]))
                                queue.append((node[0], node[1]-1))


        return res