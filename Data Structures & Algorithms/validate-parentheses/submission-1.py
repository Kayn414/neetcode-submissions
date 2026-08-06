class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        closedSym = {")":"(", "}" : "{", "]" : "["}
        stack = []

        for c in s:
            if c in closedSym:
                if stack and stack[-1] == closedSym[c]:
                    stack.pop()
                else:
                    return False
            
            else:
                stack.append(c)
        
        return True if not stack else False
        