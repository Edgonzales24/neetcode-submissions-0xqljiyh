class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        largest = 0
        numSet = set(nums)

        for n in numSet:
            if (n - 1) not in numSet:
                length = 1
                while n + length in numSet:
                    length += 1
                largest = max(largest, length)
        return largest