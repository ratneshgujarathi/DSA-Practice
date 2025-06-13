class Solution:
    def factorial(self, num: int) -> int:
        if num == 0 or num == 1:
            return 1
        
        return num * self.factorial(num-1)
    

s = Solution()
num = 5
print(s.factorial(5))