class Solution:
    def atoi(self, st, ind=0, result = 0, sign=1):
        INT_MIN = -2 ** 31
        INT_MAX = 2 ** 31 - 1

        if ind == 0:
            st = st.lstrip()
            if not st:
                return 0
            if st[ind] == '-':
                sign = -1
                return self.atoi(st, ind+1,0, sign)
            elif st[ind] == '+':
                return self.atoi(st, ind+1,0, sign)
            
        if ind >= len(st) or not st[ind].isdigit():
            return sign * result
        
        digit = ord(st[ind]) - ord('0')
        result = result * 10 + digit

        if sign == 1 and result > INT_MAX:
            return INT_MAX
        if sign == -1 and -result < INT_MIN:
            return INT_MIN
        return self.atoi(s, ind + 1, result, sign)

        




s= Solution()
case1 = '42'
case2 = '-042'
case3 = '1-42'
case4 = '1337eo8u'
case5 = 'words 987'

print(s.atoi(case1))
print(s.atoi(case2))
print(s.atoi(case3))
print(s.atoi(case4))
print(s.atoi(case5))