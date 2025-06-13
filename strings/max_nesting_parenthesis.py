class Solution:
    def max_nesting(self, st: str):
        max_depth, curr_depth = 0, 0
        for bracket in st:
            if '(' == bracket:
                curr_depth +=1
                max_depth = max(max_depth, curr_depth)
            elif ')' == bracket:
                curr_depth-=1
        return max_depth
    
ex = "(1+(2*3)+((8)/4))+1"
s =Solution()
print(s.max_nesting(ex))
