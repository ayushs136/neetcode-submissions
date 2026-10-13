class Solution:
    def maxCoins(self, nums: list[int]) -> int:

        nums = [1] + nums + [1]
        m = len(nums)
        dp = [[-1] * m for i in range(m)]

        def f(l, r):

            if l >= r - 1:
                return 0
            if dp[l][r] != -1:
                return dp[l][r]
            maxi = 0
            for i in range(l + 1, r):
                cost = (nums[l] * nums[i] * nums[r]) + f(l, i) + f(i, r)

                maxi = max(maxi, cost)

            dp[l][r] = maxi
            return dp[l][r]

        return f(0, m - 1)
