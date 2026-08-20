class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda pair : pair[1])
        lastEnd = intervals[0][1]
        cnt = 0
        
        for start, end in intervals[1:]:
            if lastEnd > start:
                cnt += 1
            else:
                lastEnd = end
        return cnt