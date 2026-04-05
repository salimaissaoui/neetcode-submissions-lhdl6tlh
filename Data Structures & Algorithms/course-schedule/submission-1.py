class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = defaultdict(list)

        for course, prereq in prerequisites:
            graph[prereq].append(course)
        
        visited = set()
        recStack = set()

        def dfs(course):
            if course in recStack:
                return False
            if course in visited:
                return True
            
            recStack.add(course)
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False
            recStack.remove(course)
            visited.add(course)
            return True
        
        for course in range(numCourses):
            if course not in visited:
                if not dfs(course):
                    return False
        return True



        