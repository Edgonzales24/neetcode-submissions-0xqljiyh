class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFF
        max_val = 0x7FFFFF

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask
        return a if a <= max_val else ~(a ^ mask)