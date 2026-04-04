class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map_nums = set()

        for num in nums:
            if num in map_nums:
                return True
        
            map_nums.add(num)
        return False
        
        

        # for i in range(0, len(nums)):
        #     if nums[i] not in map_nums:
        #         map_nums[nums[i]] = [i] 
        #     else:
        #         map_nums[nums[i]].append(i)

        # for i in nums:
        #     if i in map_nums.keys():
        #         if len(map_nums[i]) != 1:
        #             return True
        # return False    
      

        