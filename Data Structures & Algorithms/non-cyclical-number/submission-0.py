class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.sumOfSquare(n)
        while slow != fast:
            slow = self.sumOfSquare(slow)
            fast = self.sumOfSquare(fast)
            fast = self.sumOfSquare(fast)
        return True if fast == 1 else False
    
    def sumOfSquare(self, n: int) -> int:
        output = 0

        while n:
            digit = n % 10
            digit = digit ** 2
            output += digit
            n = n // 10
        return output