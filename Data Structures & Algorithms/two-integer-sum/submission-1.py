class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output_list = []
        for num1 in range(len(nums)):
            for num2 in range(len(nums)): 
                if num1 != num2:
                    if nums[num1] + nums[num2] == target:
                        output_list.append(num1)
                        output_list.append(num2)
                        return sorted(output_list)
