class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        prevHash = {} # char : last instance
        longest = 0
        l = 0
        for r in range(len(s)):
            if s[r] in prevHash:
                l = max(l, prevHash[s[r]] + 1)
            prevHash[s[r]] = r
            longest = max(longest, r - l + 1)
        return longest
            
        