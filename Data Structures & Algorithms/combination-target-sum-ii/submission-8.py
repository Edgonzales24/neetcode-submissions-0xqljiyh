class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        
        def backtrack(i, combination, currSum):
            if currSum == target:
                res.append(combination.copy())
                return
            if i >= len(candidates) or currSum > target:
                return
            
            combination.append(candidates[i])
            backtrack(i + 1, combination, currSum + candidates[i])
            combination.pop()
            
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(i + 1, combination, currSum)
        
        backtrack(0, [], 0)
        return res