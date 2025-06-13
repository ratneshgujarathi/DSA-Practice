class Solution:
    def find_longest_common_prefix(self, strs: str):
        min_length = float('inf')
        for st in strs:
            min_length = min(min_length, len(st))
        i = 0
        while i <= min_length:
            for st in strs:
                if st[i] != strs[0][i]:
                    return strs[0][:i]
            i+=1
        return strs[0][:i]
    

strs = ["flower","flow","flight"]
s = Solution()
print(s.find_longest_common_prefix(strs))