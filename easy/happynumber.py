class Solution:
    def isHappy(self, n: int) -> bool:
        sols = []
        orig = n

        while n != 1 and len(sols) == len(set(sols)):
            n = sum([int(digit) ** 2 for digit in str(n)])
            sols.append(n)
        
        if n == 1:
            return True
        
        else:
            return False