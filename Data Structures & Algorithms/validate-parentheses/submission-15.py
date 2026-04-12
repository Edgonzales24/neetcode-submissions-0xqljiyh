class Solution:
    def isValid(self, s: str) -> bool:
        pairHash = {")" : "(", "]" : "[", "}" : "{"}
        stack = []

        for c in s:
            if c in pairHash:
                if stack and pairHash[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack