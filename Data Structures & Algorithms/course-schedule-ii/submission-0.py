class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = {c: [] for c in range(numCourses)}

        result = []
        visited, cycle = set(), set()

        #do we not have to acct for the fact that prereq is nested list?
        for course1, prereq in prerequisites:
            adjList[course1].append(prereq)

        def dfs(course1): #do we not write boolean?
            if course1 in cycle:
                return False

            if course1 in visited:
                return True

            cycle.add(course1)
            
            for el in adjList[course1]:
                #this is where the recursion takes place
                if dfs(el) == False: #put here bcuz cycle might have not been there initially, could happen deeper in
                    return False
            cycle.remove(course1) #this is the individual node itself
            visited.add(course1)
            result.append(course1) #is this ok because result is initiated outside of dfs() then used again later

        #after loop is done
        for course2 in range(numCourses):
            if dfs(course2) == False:
                return []

        return result
