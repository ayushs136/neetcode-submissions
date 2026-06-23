class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        n = len(cardPoints)

        curr_sum = sum(cardPoints[:k])

        max_score = curr_sum

        for i in range(k):

            left_to_remove = cardPoints[k-1-i]
            right_to_add = cardPoints[n-1-i]

            curr_sum = curr_sum - left_to_remove + right_to_add

            max_score = max(curr_sum, max_score)
        
        return max_score