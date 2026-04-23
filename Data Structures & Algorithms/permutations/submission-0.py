class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        def generate(index):

            if len(nums) == index:
                result.append(nums[:])
                return
            
            for i in range(index, len(nums)):

                nums[i], nums[index] = nums[index], nums[i]
                generate(index+1)
                nums[i], nums[index] = nums[index], nums[i]
                

        generate(0)
        return result