class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, comb, currSum):
            if currSum == target:
                res.append(comb.copy())
                return
            if i == len(nums) or currSum > target:
                return
            
            comb.append(nums[i])
            backtrack(i, comb, currSum + nums[i])
            comb.pop()
            backtrack(i + 1, comb, currSum)

        backtrack(0, [], 0)
        return res
