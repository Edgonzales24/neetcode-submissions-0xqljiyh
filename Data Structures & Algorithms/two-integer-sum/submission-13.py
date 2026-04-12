class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevNum = {} # num : index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevNum:
                return [prevNum[diff], i]
            prevNum[n] = i