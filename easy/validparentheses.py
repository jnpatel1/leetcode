class Solution:
    def isValid(self, s: str) -> bool:
        bracs = []
        bracsDict = {"}": "{", ")": "(", "]": "["}

        for brac in s:
            if brac in "([{":
                bracs.append(brac)
            
            elif bracs:
                if bracsDict[brac] == bracs[-1]:
                    bracs.pop()
                else:
                    return False
            
            else:
                return False
        
        return (not bracs)