class Solution:
    def rob(self, nums: List[int]) -> int:

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
