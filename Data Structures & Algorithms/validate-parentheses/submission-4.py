class Solution:
    def isValid(self, s: str) -> bool:
        pairHash = {")" : "(", "]" : "[", "}" : "{"}
        stack = []

        for c in s:
            if stack and c in pairHash:
                if stack[-1] == pairHash[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack