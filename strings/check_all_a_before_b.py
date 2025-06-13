class Solution:
    def checkString(self, s: str) -> bool:
        '''Given a string s consisting of only the characters 'a' and 'b', return true if every 'a' should appears before every 'b' in the string. Otherwise, return false.'''
        flag = 0
        for letter in s:
            if letter == 'b':
                flag = 1
            
            if flag == 1 and letter == 'a':
                return False
        return True
    

s = Solution()
example = 'aaabbb'
example1 = 'abab'