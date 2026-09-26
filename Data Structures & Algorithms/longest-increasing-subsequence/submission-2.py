class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)

        dp = [1] * n
        maxi = 1

        for i in range(n):
            for prev in range(i):

                if nums[i] > nums[prev]:
                    dp[i] = max(dp[i], 1 + dp[prev])

            maxi = max(maxi, dp[i])

        return maxi
