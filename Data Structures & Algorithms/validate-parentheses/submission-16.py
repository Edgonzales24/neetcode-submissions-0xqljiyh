class Solution:
    def isValid(self, s: str) -> bool:
        pairMp = {")" : "(", "]" : "[", "}" : "{"}
        stack = []

        for c in s:
            if c in pairMp:
                if stack and pairMp[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack