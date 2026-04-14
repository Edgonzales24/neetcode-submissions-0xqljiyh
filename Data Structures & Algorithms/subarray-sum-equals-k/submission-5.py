class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSums = {0 : 1} # prefix : count
        currSum = 0
        res = 0

        for n in nums:
            currSum += n
            diff = currSum - k
            res += prefixSums.get(diff, 0)
            prefixSums[currSum] = prefixSums.get(currSum, 0) + 1
        
        return res