class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        result = []
        combination = []

        s = set()

        def findCombination(index, target):

            if index >= len(nums) or target < 0:
                return

            if target == 0:
                if tuple(combination) not in s:
                    s.add(tuple(combination))
                    result.append(list(combination))
                return

            combination.append(nums[index])
            findCombination(index + 1, target - nums[index])
            findCombination(index, target - nums[index])
            combination.pop()
            findCombination(index + 1, target)

        findCombination(0, target)

        return result
