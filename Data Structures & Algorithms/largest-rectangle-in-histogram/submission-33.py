class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                stackI, stackH = stack.pop()
                area = max(area, stackH * (i - stackI))
                start = stackI
            stack.append((start, h))
        
        for i, h in stack:
            area = max(area, h * (len(heights) - i))
        return area