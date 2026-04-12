class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {} # char : index
        maxLength = 0

        l = 0
        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l)
            mp[s[r]] = r
            maxLength = max(maxLength, r - l + 1)
        return maxLength
         
