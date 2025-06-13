class Solution:
    def find_repeat_missing_num(self, arr: list) -> list:
        s, sn = 0, (len(arr) * (len(arr) + 1)) // 2
        s2, s2n = 0, (len(arr) * (len(arr)+1) * (2*len(arr)+1)) // 6

        for i in arr:
            s += i
            s2 += i*i

        x_y = s - sn
        x2_y2 = s2 - s2n

        x2_y2 = x2_y2 // x_y
        x = x_y - x2_y2


        return [x,y]

s = Solution()
arr = [1,3,4,5,6,6]
print(s.find_repeat_missing_num(arr))