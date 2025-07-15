class Solution:
    def fib(self, n, dp):
        if n <= 1:
            return n
        if dp[n] != -1:
            return dp[n]
        dp[n] = self.fib(n-1, dp) + self.fib(n-2, dp)
        return dp[n]
    
s = Solution()
n = 6
dp = [-1]*(n+1)
ans = s.fib(n, dp)
print(ans)
        
