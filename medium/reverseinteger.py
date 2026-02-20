class Solution:
    def reverse(self, x: int) -> int:
        sint = str(x)

        if x < 0:
            ans = -1 * int(str(abs(x))[::-1])
            if ans >= (-(2 ** 31)) and ans <= ((2 ** 31) - 1):
                return ans
            
            else:
                return 0
        
        else:
            ans = int(sint[::-1])
            if ans >= (-(2 ** 31)) and ans <= ((2 ** 31) - 1):
                return ans
            
            else:
                return 0