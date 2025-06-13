class Solution:
    def roman_num(self, roman_num):
        roman_map = {"I":1,
                    "V":5,
                    "X":10,
                    "L":50,
                    "C":100,
                    "D":500,
                    "M":1000}
        curr, prev = 0, 0
        ans = 0
        for i in range(len(roman_num) - 1, -1 , -1):
            curr = roman_map[roman_num[i]]
            if curr < prev:
                ans -= curr
            else:
                ans += curr
            prev = curr

        return ans
    

s = Solution()
ex = "MCMXCIV"
print(s.roman_num(ex))