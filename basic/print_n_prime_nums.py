class Solution:
    def nth_prime_number(self, n):
        cnt = 0 
        num = 2

        while cnt < n:
            if self.is_prime(num):
                cnt+=1
            num+=1

        return num - 1
            
    
    def print_n_prime_numbers(self, n):
        cnt = 0 
        num = 2

        while cnt < n:
            if self.is_prime(num):
                print(num)
                cnt+=1
            num+=1
            
            

    def is_prime(self, num):
        i = 1
        cnt = 0
        while i*i <= num:
            if num % i == 0:
                cnt += 1
                if num / i != i:
                    cnt+=1

            if cnt > 2:
                return False
            
            i+=1

        return cnt == 2 
    

s = Solution()
print(s.is_prime(7))
s.print_n_prime_numbers(7)
print(s.nth_prime_number(7))