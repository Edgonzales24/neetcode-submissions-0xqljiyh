class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, curr, totalSum):
            if totalSum == target:
                res.append(curr.copy())
                return
            if i >= len(nums) or totalSum > target:
                return
            
            curr.append(nums[i])
            backtrack(i, curr, totalSum + nums[i])
            curr.pop()
            backtrack(i + 1, curr, totalSum)
        
        backtrack(0, [], 0)
        return res