class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0:
            return False

        while n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
            for hi in [2,3,5]:
                if n % hi == 0:
                    n /= hi
        
        if n == 1:
            return True

        else:
            return False
        