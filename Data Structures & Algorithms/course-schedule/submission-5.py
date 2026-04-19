class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i : [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        cycle, visited = set(), set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            
            cycle.add(crs)
            for nei in preMap[crs]:
                if not dfs(nei):
                    return False
            cycle.remove(crs)
            visited.add(crs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True