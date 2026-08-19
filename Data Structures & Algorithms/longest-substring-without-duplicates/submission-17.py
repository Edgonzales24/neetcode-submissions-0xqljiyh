class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = {} # char : idx
        longest = 0
        l = 0

        for r in range(len(s)):
            if s[r] in count:
                l = max(l, count[s[r]] + 1)
            count[s[r]] = r
            longest = max(longest, r - l + 1)
        return longest
