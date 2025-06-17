class Solution:
    def print_a_n_times(self, N: int):
        if N == 0:
            return 
        print('a', N)
        self.print_a_n_times(N-1)

    def print_name_n_times(self, N: int, name: str):
        if N == 0:
            return 
        print(name, N)
        self.print_name_n_times(N-1, name)

    def print_n_numbers(self, n):
        if n == 0:
            return 
        print(n)
        self.print_n_numbers(n-1)

    def print_0_2_n_numbers(self, n, i=1):
        if i > n:
            return 
        print(i)
        self.print_0_2_n_numbers(n, i+1)

s= Solution()
case1 = 5
# s.print_name_n_times(case1, 'ratnesh')
s.print_n_numbers(case1)