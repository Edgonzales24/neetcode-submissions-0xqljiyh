class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        numSet = set(nums)

        for n in numSet:
            longest = 0
            if (n - 1) not in numSet:
                longest = 1
                while (n + longest) in numSet:
                    longest += 1
            res = max(res, longest)
        return res