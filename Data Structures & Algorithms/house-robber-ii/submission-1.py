class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def rob_(nums):
            n = len(nums)
            if n == 1:
                return nums[0]

            prev2 = nums[0]
            prev = max(nums[0], nums[1])
            for i in range(2, n):

                pick = nums[i] + prev2
                not_pick = prev

                curr = max(pick, not_pick)
                prev2 = prev
                prev = curr

            return prev

        n = len(nums)
        if n == 1:
            return nums[0]

        for i in range(n):
            if i == 0:
                first_nums = nums[1:]

            if i == n - 1:
                last_nums = nums[: n - 1]

        return max(rob_(first_nums), rob_(last_nums))
