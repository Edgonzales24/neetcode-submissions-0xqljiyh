class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # index, height
        maxArea = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                stackI, stackH = stack.pop()
                maxArea = max(maxArea, (i - stackI) * stackH)
                start = stackI
            stack.append((start, h))
        
        for i, h in stack:
            maxArea = max(maxArea, (len(heights) - i) * h)
        return maxArea