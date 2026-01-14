class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        i = 0
        if n == 0:
            return False
        while n % 2 == 0:
            n /= 2
            
            i += 1
        
        if n == 1:
            return True
        
        else:
            return False