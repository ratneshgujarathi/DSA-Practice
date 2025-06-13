class Solution:
    def check_rotated(self, strs, goal):
        temp = ''
        for i in range(len(strs)):
            temp += strs[i]
            rotated = strs[i+1:] + temp
            if rotated == goal:
                return True
        return False
    

s= Solution()
ex = "abcde"
goal = "cdeab"
print(s.check_rotated(ex, goal))