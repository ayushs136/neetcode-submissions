class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefixMax = [-1] * n
        suffixMax = [-1] * n

        prefixMax[0] = height[0]
        for i in range(1, n):
            prefixMax[i] = max(prefixMax[i - 1], height[i])

        suffixMax[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            suffixMax[i] = max(suffixMax[i + 1], height[i])

        total = 0

        for i in range(n):

            leftMax = prefixMax[i]
            rightMax = suffixMax[i]

            if height[i] < leftMax and height[i] < rightMax:
                total += min(leftMax, rightMax) - height[i]

        return total
