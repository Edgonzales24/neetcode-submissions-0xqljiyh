class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        comb = []
        candidates.sort()

        def backtrack(i, totalSum):
            if totalSum == target:
                res.append(comb.copy())
                return
            if i >= len(candidates) or totalSum > target:
                return
            
            comb.append(candidates[i])
            backtrack(i + 1, totalSum + candidates[i])
            comb.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(i + 1, totalSum)
        
        backtrack(0, 0)
        return res
