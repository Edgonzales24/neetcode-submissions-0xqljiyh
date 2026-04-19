class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = {0 : 1} # sum : occured
        res = 0
        currSum = 0

        for n in nums:
            currSum += n
            diff = currSum - k
            if diff in prefixSum:
                res += prefixSum[diff]
            prefixSum[currSum] = 1 + prefixSum.get(currSum, 0)
        return res