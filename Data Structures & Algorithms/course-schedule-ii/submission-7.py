class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i : [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            adj[crs].append(pre)
        
        visited, cycle = set(), set()
        res = []

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            
            cycle.add(crs)
            for pre in adj[crs]:
                if not dfs(pre):
                    return False
            res.append(crs)
            cycle.remove(crs)
            visited.add(crs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return res