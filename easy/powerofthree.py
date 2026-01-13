class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        exp = 0

        while 3 ** exp <= n and 3 ** exp != n:
            exp += 1

        if 3 ** exp == n:
            return True
        
        else:
            return False