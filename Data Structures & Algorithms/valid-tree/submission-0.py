class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Check edges
        if len(edges) != n - 1:
            return False
        
        visited = set()

        
        
        
        adj_list = defaultdict(list)
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        def dfsCycle(node, parent, adj_list, visited):
            visited.add(node)

            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    if dfsCycle(neighbor, node, adj_list, visited):
                        return True
                elif neighbor != parent:
                    return True
            return False

        if dfsCycle(0,-1,adj_list, visited):
            return False
        
        return len(visited) == n


        
        


        