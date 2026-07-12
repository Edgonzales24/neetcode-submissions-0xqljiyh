class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.sumOfSquare(n)
        
        while slow != fast:
            slow = self.sumOfSquare(slow)
            fast = self.sumOfSquare(self.sumOfSquare(fast))
        return fast == 1
        
    def sumOfSquare(self, n: int) -> int:
        res = 0
        while n:
            digit = n % 10
            res += digit ** 2
            n = n // 10
        return res