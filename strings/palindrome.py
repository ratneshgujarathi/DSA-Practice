class Solution:
    def check_palindrome(self, string: str) -> bool:
        length = len(string)
        pointer = 0
        while pointer < length / 2:
            if string[pointer] != string[length - pointer - 1]:
                return False
            pointer+=1
        return True
    

s = Solution()
example = "abcacba"
print(s.check_palindrome(example))