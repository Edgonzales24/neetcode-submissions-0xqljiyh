class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = [] # [start, height]

        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                stackI, stackH = stack.pop()
                res = max(res, (i - stackI) * stackH)
                start = stackI
            stack.append([start, h])
        
        for i, h in stack:
            res = max(res, (len(heights) - i) * h)
        
        return res