class Solution:
    def isValid(self, s: str) -> bool:
        parHash = {")" : "(", "]" : "[", "}" : "{"}
        stack = []

        for c in s:
            if stack and c in parHash:
                if stack[-1] == parHash[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack