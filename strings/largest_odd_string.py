class Solution:
    def largest_odd_num(self, st: str) -> int:
        i = len(st) - 1
        while i>=0 and int(st[i]) & 1 == 0:
            i-=1
        return st[:i+1]
       
    
s = Solution()
st = "42067"
print(s.largest_odd_num(st))