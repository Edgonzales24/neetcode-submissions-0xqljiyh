class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {} # char : last instance
        longest = 0
        l = 0

        for r in range(len(s)):
            if s[r] in mp:
                l = max(l, mp[s[r]] + 1)
            mp[s[r]] = r
            longest = max(longest, r - l + 1)
        return longest