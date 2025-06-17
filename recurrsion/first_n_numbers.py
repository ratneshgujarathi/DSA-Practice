class Solution:
    def sum_first_n_number(self, n):
        if n == 0:
            return n
        return n + self.sum_first_n_number(n-1)

    def fact_n_number(self, n):
        if n < 2:
            return 1
        return n * self.fact_n_number(n-1)

    def fibonacci_n_number(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        return self.fibonacci_n_number(n-1) + self.fibonacci_n_number(n-2)


s = Solution()
case1 = 6
print(s.sum_first_n_number(case1))
print(s.fact_n_number(case1))
print(s.fibonacci_n_number(case1))