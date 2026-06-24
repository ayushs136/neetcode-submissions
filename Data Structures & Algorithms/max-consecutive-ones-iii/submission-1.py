class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = max_len = zeros = 0
        for right in range(n):

            if nums[right] == 0:
                zeros += 1

            if zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            if zeros <= k:

                length = right - left + 1

                max_len = max(max_len, length)

        return max_len
