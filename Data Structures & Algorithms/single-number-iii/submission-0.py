class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        

        xorr = 0
        b1 = 0
        b2 = 0
        for n in nums:
            xorr^=n

        rightM = xorr^(xorr-1)&xorr

        for n in nums:

            if rightM&n:
                b1^=n
            else:
                b2^=n

        return [b1, b2]