class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda x: x[1])

        lastEnd = intervals[0][1]
        n = len(intervals)
        count = 1
        for i in range(1, n):
            if lastEnd <= intervals[i][0]:
                count += 1
                lastEnd = intervals[i][1]

        return n - count
