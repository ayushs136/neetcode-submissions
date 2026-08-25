class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        prev = nums[0]
        prev2 = 0
        for i in range(1, n):
            pick = nums[i]
            if i - 2 >= 0:
                pick += prev2

            not_pick = prev
            curr = max(pick, not_pick)
            prev2 = prev
            prev = curr

        return prev
