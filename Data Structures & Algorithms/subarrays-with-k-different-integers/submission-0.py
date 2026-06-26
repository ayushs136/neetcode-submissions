class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def helper(nums, k):
            if k < 0:
                return 0
            n = len(nums)
            left = 0
            max_len = 0
            count = defaultdict(int)

            for right in range(n):

                count[nums[right]] += 1

                while len(count) > k:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        count.pop(nums[left])
                    left += 1

                max_len += right - left + 1

            return max_len

        return helper(nums, k) - helper(nums, k - 1)
