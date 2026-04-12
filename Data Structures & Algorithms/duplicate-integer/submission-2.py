class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        freq = defaultdict(int)


        for num in nums:
            freq[num] += 1
        

        for value in freq.values():
            if value > 1:
                return True
        

        return False