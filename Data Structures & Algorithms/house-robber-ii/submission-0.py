class Solution:
    def rob(self, nums: List[int]) -> int:
        def dp(nums):
            n = len(nums)

            prev = nums[0]
            prev2 = 0

            for i in range(1, n):
                pick = nums[i]
                if i > 1:
                    pick += prev2
                not_pick = prev

                curr = max(pick, not_pick)

                prev2 = prev
                prev = curr

            return prev

        n = len(nums)
        if n == 1:
            return nums[0]
        first_nums, last_nums = [], []
        for i in range(n):
            if i != 0:
                first_nums.append(nums[i])
            if i != n - 1:
                last_nums.append(nums[i])

        return max(dp(first_nums), dp(last_nums))
