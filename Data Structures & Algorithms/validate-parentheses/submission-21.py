class Solution:
    def isValid(self, s: str) -> bool:
        pairMp = {")" : "(", "]" : "[", "}" : "{"}
        stack = []

        for c in s:
            if c in pairMp:
                if stack and stack[-1] == pairMp[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack
