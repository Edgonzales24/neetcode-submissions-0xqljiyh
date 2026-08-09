class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxF = 0
        mp = {}
        longest = 0
        
        l = 0
        for r in range(len(s)):
            mp[s[r]] = mp.get(s[r], 0) + 1
            maxF = max(maxF, mp[s[r]])

            if (r - l + 1) - maxF > k:
                mp[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest