class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        freq = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in freq:
                return [freq[diff], i]
            
            freq[nums[i]] = i