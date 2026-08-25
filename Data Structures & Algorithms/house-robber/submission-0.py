class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * n

        def r(i, dp):
            if i == 0:
                return nums[i]
            if i < 0:
                return 0
            if dp[i] != -1:
                return dp[i]

            pick = nums[i] + r(i - 2, dp)
            not_pick = r(i - 1, dp)
            dp[i] = max(pick, not_pick)

            return dp[i]

        return r(n - 1, dp)
