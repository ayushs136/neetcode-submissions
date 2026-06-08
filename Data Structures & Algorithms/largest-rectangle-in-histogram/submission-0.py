class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        def nextSmallerElement(nums):

            stack = []
            n = len(nums)
            res = [n] * n

            for i in range(n - 1, -1, -1):
                while stack and nums[stack[-1]] >= nums[i]:
                    stack.pop()
                if stack: 
                    res[i] = stack[-1]

                stack.append(i)

            return res

        def prevSmallerElement(nums):

            stack = []
            n = len(nums)
            res = [-1] * n

            for i in range(n):
                while stack and nums[stack[-1]] >= nums[i]:
                    stack.pop()
                if stack:
                    res[i] = stack[-1]

                stack.append(i)

            return res

        pse = prevSmallerElement(heights)
        nse = nextSmallerElement(heights)

        maxi = 0
        for i in range(len(heights)):
            ans = heights[i] * (nse[i] - pse[i] - 1)
            maxi = max(ans, maxi)

        return maxi
