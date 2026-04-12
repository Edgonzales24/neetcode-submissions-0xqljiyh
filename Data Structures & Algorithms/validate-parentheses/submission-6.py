class Solution:
    def isValid(self, s: str) -> bool:
        pairHash = {")" : "(", "]" : "[", "}" : "{"}
        stack = []

        for c in s:
            if stack and c in pairHash:
                if pairHash[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack