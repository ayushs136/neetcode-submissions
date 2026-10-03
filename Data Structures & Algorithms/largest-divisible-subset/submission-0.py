class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:

        n = len(nums)
        nums.sort()
        parent = list(range(n))

        last_idx = 0
        dp = [1] * (n + 1)
        maxi = 0
        for i in range(n):
            for prev in range(i):
                if nums[i] > nums[prev] and nums[i] % nums[prev] == 0:
                    dp[i] = 1 + dp[prev]
                    parent[i] = prev

            if maxi < dp[i]:
                maxi = dp[i]
                last_idx = i

        res = []

        curr = last_idx
        while parent[curr] != curr:
            res.append(nums[curr])
            curr = parent[curr]

        res.append(nums[curr])

        return res[::-1]
