class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(numCourses)}
        res = []

        for course, prereq in prerequisites:
            graph[course].append(prereq)

        visited = set()
        path = set()

        
        def dfs(course):
            if course in path:
                return False
            
            if course in visited:
                return True

            path.add(course)

            for prereq in graph[course]:
                if dfs(prereq) == False:
                    return False

            path.remove(course)
            visited.add(course)
            res.append(course)

            return True

        for course in range(numCourses):
            if dfs(course) == False:
                return []


        return res   

                