class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        total = sum(nums)

        if (total - target) % 2 != 0 or (total - target) < 0:
            return 0

        s1 = (total - target) // 2

        prev = [0] * (s1 + 1)

        prev[0] = 1

        for i in range(n):
            curr = [0] * (s1 + 1)
            for tar in range(s1 + 1):
                not_pick = prev[tar]

                pick = 0
                if nums[i] <= tar:
                    pick = prev[tar - nums[i]]

                curr[tar] = pick + not_pick
            prev = curr

        if (total - target) % 2 == 0 or (total - target) >= 0:
            return prev[s1]
