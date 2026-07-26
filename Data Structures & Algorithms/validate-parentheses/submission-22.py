class Solution:
    def isValid(self, s: str) -> bool:
        pair = {")" : "(", "]" : "[", "}" : "{"}
        stack = []

        for c in s:
            if c in pair:
                if stack and pair[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack