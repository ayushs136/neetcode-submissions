class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []
        n = len(heights)
        maxArea = 0
        for i, h in enumerate(heights):
            while stack and stack[-1][1] >= h:
                index, height = stack.pop()
                pse = stack[-1][0] if stack else -1
                nse = i

                maxArea = max(maxArea, height * (nse - pse - 1))

            stack.append((i, h))

        while stack:
            index, height = stack.pop()
            pse = stack[-1][0] if stack else -1
            nse = n
            maxArea = max(maxArea, height * (nse - pse - 1))

        return maxArea
