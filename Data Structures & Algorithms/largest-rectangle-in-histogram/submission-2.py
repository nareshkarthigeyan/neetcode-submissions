from collections import deque
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 0:
            return 0
        if len(heights) == 1:
            return heights[0]
        
        maxArea = 0

        stack = []
        for i, v in enumerate(heights):
            if not stack or v > stack[-1][-1]:
                stack.append((i, v))
            else:
                ix = None
                while stack and stack[-1][-1] >= v:
                    idx, val = stack.pop()
                    maxArea = max(val * (i - idx), maxArea)
                    ix = idx
                stack.append((ix, v))

        n = len(heights)

        while stack:
            idx, val = stack.pop()
            area = (n - idx) * val
            maxArea = max(area, maxArea)
        
        return maxArea
