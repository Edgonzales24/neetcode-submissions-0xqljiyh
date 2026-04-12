class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = [] # index, height

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                stackInd, stackH = stack.pop()
                currArea = stackH * (i - stackInd)
                res = max(currArea, res)
                start = stackInd
            stack.append((start, h))
        
        for i, h in stack:
            res = max(res, (h * (len(heights) - i)))
        return res