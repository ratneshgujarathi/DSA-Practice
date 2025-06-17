class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        hash = {}
        l, r = 0, 0
        for r in range(len(s)):
            if s[r] in hash and hash[s[r]] >= l:
                l = hash[s[r]] + 1
            hash[s[r]] = r
            max_length = max(max_length, r - l + 1)

        return max_length

s = Solution()
print(s.lengthOfLongestSubstring('abcabcbb'))