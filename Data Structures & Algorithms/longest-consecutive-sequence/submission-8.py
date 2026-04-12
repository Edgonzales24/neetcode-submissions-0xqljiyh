class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0

        for n in nums:
            if n - 1 not in nums:
                longest = 1
                while n + longest in nums:
                    longest += 1
                res = max(res, longest)
        return res