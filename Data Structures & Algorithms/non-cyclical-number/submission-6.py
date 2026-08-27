class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.sumOfSquares(n)
        while slow != fast:
            slow = self.sumOfSquares(slow)
            fast = self.sumOfSquares(self.sumOfSquares(fast))
        return fast == 1
    
    def sumOfSquares(self, n):
        res = 0
        while n:
            digit = n % 10
            res += digit ** 2
            n = n // 10
        return res
