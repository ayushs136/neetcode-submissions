class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        n = len(prices)

        front1 = [0, 0]
        front2 = [0, 0]

        for i in range(n - 1, -1, -1):

            curr = [0, 0]
            
            curr[1] = max(-prices[i] + front1[0], front1[1])
            curr[0] = max(prices[i] + front2[1], front1[0])

            front2 = front1
            front1 = curr

        return curr[1]
