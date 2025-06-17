class Solution:
    def check_palindrome(self, st, i=0):
        if i >= len(st) // 2:
            return True
        
        if st[i] != st[len(st)-i-1]:
            return False
        
        return self.check_palindrome(st, i+1)
    

s = Solution()
print(s.check_palindrome("abaaba"))