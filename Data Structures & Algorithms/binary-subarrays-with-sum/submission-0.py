class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        def helper(nums, goal):
            if goal<0:
                return 0
            count = sum = left = 0
            for right in range(len(nums)):
                sum += nums[right]

                while sum > goal:
                    sum -= nums[left]
                    left += 1

                if sum <= goal:
                    count += right - left + 1

            return count

        return helper(nums, goal) - helper(nums, goal - 1)
