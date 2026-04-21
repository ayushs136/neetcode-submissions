class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        curr = []

        def generate(index):

            if len(nums) == index:
                res.append(curr[:])
                return

            curr.append(nums[index])
            generate(index+1)
            curr.pop()
            generate(index+1)


        generate(0)
        return res