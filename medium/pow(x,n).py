class Solution:
    def myPow(self, x: float, n: int) -> float:
        leftover = 1

        if x == 1 or n == 0:
            return 1
        
        if n == 1:
            return x
        
        if n < 0:
            n = abs(n)
            x = 1/x

        while n > 1:
            if n % 2 == 1:
                leftover *= x
                n -= 1
            
            else:
                x = x ** 2
                n /= 2
             
        return x * leftover