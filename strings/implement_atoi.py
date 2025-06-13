class Solution:
    def atoi(self, st: str):
        st = st.lstrip()
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31
        n = len(st)
        sign = 1
        i = 0

        if len(st) == 0:
            return 0
        
        if st[0] == '-':
            sign = -1
            i+=1
        elif st[0] == '+':
            i += 1
        num = 0
        while i < n and st[i].isdigit():
            num = num * 10 + int(st[i])
            i+=1

        num = num * sign
        
        return max(INT_MIN, min(INT_MAX, num))
    

s = Solution()
example1 = '42'
example2 = '-042'
example3 = '1337c0d3'
example4 = '0-1'
example5 = 'words and 987'

print(s.atoi(example3))