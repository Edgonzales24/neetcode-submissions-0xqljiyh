class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i : [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adj[crs].append(pre)
        
        visited, cycle = set(), set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            
            cycle.add(crs)
            for pre in adj[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            visited.add(crs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True