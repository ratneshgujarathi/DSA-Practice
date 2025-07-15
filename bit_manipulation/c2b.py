class Solution:
    def convert2binary(self, num :int) -> str:
        if num == 0:
            return '0'
        res = ''
        while num > 0:
            if num % 2 == 1:
                res = '1'+ res
            else:
                res = '0' + res

            num = num // 2
        return res
    
    def convert2decimal(self, s: str) -> int:
        num = 0
        for i in range(len(s) - 1, -1, -1):
            num += int(s[i]) * (2 ** (len(s) - 1 - i))

        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if num > INT_MAX:
            return INT_MAX

        return num
    


s = Solution()
ans = s.convert2binary(13)
ans1 = s.convert2decimal('1101')
print(ans1)