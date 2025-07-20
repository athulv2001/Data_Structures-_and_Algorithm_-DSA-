from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        visited = [0] * numCourses  # 0=unvisited, 1=visiting, 2=visited

        def dfs(course):
            if visited[course] == 1:
                return False  # cycle detected
            if visited[course] == 2:
                return True  # already processed

            visited[course] = 1  # mark as visiting
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False
            visited[course] = 2  # mark as done
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
