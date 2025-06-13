class Solution:
    def remove_outer_parenthesis(self, st: str):
        count = 0
        ans = ''
        for bracket in st:
            if '(' == bracket:
                if count != 0:
                    ans+=bracket
                count+=1
            else:
                count-=1
                if count != 0:
                    ans+=bracket
        return ans
    
s= Solution()
ex = "(()())(())"
print(s.remove_outer_parenthesis(ex))