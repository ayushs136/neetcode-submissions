class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        ahead = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            curr = [0] * (n + 1)
            for prev in range(i - 1, -2, -1):
                length = 0 + ahead[prev + 1]

                if prev == -1 or nums[i] > nums[prev]:
                    length = max(length, 1 + ahead[i + 1])

                curr[prev + 1] = length
            ahead = curr

        return ahead[0]
