from typing import List
from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjacency = defaultdict(list)
        in_degree = [0] * numCourses

        for course, prereq in prerequisites:
            adjacency[prereq].append(course)
            in_degree[course] += 1

        queue = deque()
        for course in range(numCourses):
            if in_degree[course] == 0:
                queue.append(course)

        if not queue:
            return False

        completed = 0
        while queue:
            course = queue.popleft()
            completed += 1
            for next_course in adjacency[course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)

        return completed == numCourses
