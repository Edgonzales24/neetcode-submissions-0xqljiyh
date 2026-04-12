class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l = 0
        r = len(numbers) - 1


        while l < r:

            # [1, 2, 3, 4] target = 3
            summ = numbers[l] + numbers[r]
            
            if target < summ:
                r -= 1
            
            elif target > summ:
                l += 1
            
            else:
                return [l + 1, r + 1]

        