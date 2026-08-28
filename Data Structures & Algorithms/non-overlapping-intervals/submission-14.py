class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda pair : pair[1])
        res = 0
        lastEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if lastEnd > start:
                res += 1
            else:
                lastEnd = end
        return res