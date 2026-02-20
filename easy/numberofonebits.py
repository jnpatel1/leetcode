class Solution:
    def hammingWeight(self, n: int) -> int:
        sol = ""

        while n > 0:
            if n % 2 == 1:
                sol += "1"
                n = n // 2
            
            else:
                sol += "0"
                n /= 2
        
        return sol.count("1")