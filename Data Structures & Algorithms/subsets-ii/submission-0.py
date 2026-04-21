class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []

        def generate(index):

            if len(nums) == index:
                res.append(curr[:])
                return

            curr.append(nums[index])
            generate(index+1)
            curr.pop()

            idx = index +1
            while idx<len(nums) and nums[idx] == nums[index]:
                idx+=1
            generate(idx)

        nums.sort()
        generate(0)
        return res