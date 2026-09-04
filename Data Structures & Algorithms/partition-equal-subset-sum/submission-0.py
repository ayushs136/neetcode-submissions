class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        n = len(nums)
        total_sum = sum(nums)

        if total_sum % 2 != 0:
            return False
        half_sum = total_sum // 2

        def getSubsetSum(idx, sum):

            prev = [False] * (sum + 1)
            prev[0] = True

            for i in range(1, n):
                curr = [False] * (sum + 1)
                curr[0] = True

                for target in range(1, sum + 1):
                    not_take = prev[target]
                    take = False
                    if nums[i] <= target:
                        take = prev[target - nums[i]]

                    curr[target] = take or not_take

                prev = curr
            return prev[sum]

        return getSubsetSum(n - 1, half_sum)
