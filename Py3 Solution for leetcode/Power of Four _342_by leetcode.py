class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        x_int = pow(n,0.5)
        return n>0 and 2**31%n==0 and x_int == int(x_int)