class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if dividend == INT_MIN and divisor ==  -1:
            return INT_MAX

        negativeFlag = (dividend < 0) ^ (divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        quotient = 0

        while dividend >= divisor:
            tmp, multiple = divisor, 1
            while dividend >= (tmp << 1):
                tmp <<= 1
                multiple <<= 1
            dividend -= tmp
            quotient += multiple
        
        return -quotient if negativeFlag else quotient 


        if divisor == 1 or divisor == -1 or dividend == 0: 
            if divisor == -1:
                if dividend < 0:
                    return -dividend
                return -dividend
            return dividend

        signFlag = 0
        quotient = 0

        if dividend < 0:
            signFlag += 1
            dividend *= -1
        if divisor < 0:
            signFlag += 1
            divisor *= -1
        
        while dividend - divisor >= 0:
            quotient += 1
            dividend -= divisor
        
        if signFlag == 1: 
            return -quotient

        return quotient

        
