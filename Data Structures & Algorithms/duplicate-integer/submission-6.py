class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prevNum = set()

        for n in nums:
            if n in prevNum:
                return True
            prevNum.add(n)
        return False