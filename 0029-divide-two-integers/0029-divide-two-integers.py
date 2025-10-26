class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if dividend <= INT_MIN and divisor == -1:
            return INT_MAX
        
        negativeFlag = (dividend < 0) ^ (divisor < 0)
        quotient = 0
        dividend = abs(dividend)
        divisor = abs(divisor)

        while divisor <= dividend:
            tmp = divisor
            multiple = 1
            while dividend >= (tmp << 1):
                tmp <<= 1
                multiple <<= 1
            divisor -= tmp
            quotient += multiple

        return -quotient if negativeFlag else quotient
        