class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        left = right = 0

        m = len(g)
        n = len(s)

        s = sorted(s)
        g = sorted(g)

        while left<n and right<m:

            if s[left]>=g[right]:
                right+=1
            left+=1

        return right

        