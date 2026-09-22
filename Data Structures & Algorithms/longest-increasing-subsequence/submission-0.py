class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [[-1] * n for _ in range(n)]

        def f(i, prev):
            if i >= n:
                return 0
            if dp[i][prev] != -1:
                return dp[i][prev]
            leng = 0 + f(i + 1, prev)

            if prev == -1 or nums[i] > nums[prev]:
                leng = max(leng, 1 + f(i + 1, i))
            dp[i][prev] = leng
            return dp[i][prev]

        return f(0, -1)
