from collections import defaultdict
from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        res = 0
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)  # 🔑 make it undirected

        visited = set()

        def exploreNode(node):
            if node in visited:
                return
            visited.add(node)  # 🔑 mark node as visited
            for val in adj[node]:
                exploreNode(val)
             
        for i in range(n):  # 🔑 iterate all nodes, including isolated
            if i not in visited:
                res += 1
                exploreNode(i)
        
        return res