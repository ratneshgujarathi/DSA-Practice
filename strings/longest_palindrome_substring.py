class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        
        longest = ''
        for i in range(n):
            for j in range(i, n):
                sub_str = s[i:j+1]
                if sub_str == sub_str[::-1] and len(sub_str) > len(longest):
                    longest = sub_str

        return longest
    
s = Solution()
print(s.longestPalindrome('babad'))