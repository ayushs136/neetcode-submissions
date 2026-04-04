class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        def findInRow(nums, target, n):

            low = 0
            high = n-1
            if target>nums[high]:
                return False
            
            while low<=high:
                mid = (low+high)//2

                if nums[mid] == target:
                    return True

                elif nums[mid]>target:
                    high = mid-1
                else:
                    low = mid+1


        for i in range(m):

            if findInRow(matrix[i], target, n):
                return True
        
        return False
                
