class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range (numCourses)]

        for course,prerequisite in prerequisites:
            graph[prerequisite].append(course)
            
        state=[0]* numCourses
        result=[]

        def dfs (course):
            if state[course]==1:
                return False
            if state[course]==2:
                return True
            state[course]=1

            for next_course in graph[course]:
                if not  dfs(next_course):
                    return False
            state[course]=2
            result.append(course)
            return True

        for course in range(numCourses):
            if state[course]==0:
                if not dfs(course):
                    return []
        result.reverse()
        return result



        