class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:        
        maxArea = 0
        heights.append(0)
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

        # n = len(heights)

        # while stack:
        #     idx, val = stack.pop()
        #     area = (n - idx) * val
        #     maxArea = max(area, maxArea)
        
        return maxArea
