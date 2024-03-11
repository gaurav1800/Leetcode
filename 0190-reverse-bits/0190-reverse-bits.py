class Solution:
    def reverseBits(self, n: int) -> int:
        
        def f(n,r,count):
            if n<1:
                return r<<(32-count)
            return f(n>>1,(r<<1)|(n&1),count+1)
        return f(n,0,0)
        
        
#         another implementation
#         result = 0
        
#         for i in range(32):
#             bit  =  (n >> i ) & 1
#             result = result | (bit << (31-i))
        
#         return result