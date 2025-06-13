class Solution:
    def reverse_inplace(self, string: str):
        start, end = 0, len(string)
        while start < end:
            string[start], string[end] = string[end], string[start]

s = Solution()
example = "abcde"

print(s.reverse_inplace(example))