class Solution:
    def valid_parenthesis(self, brackets: str) -> bool:
        splitted = [*brackets]
        map = {")": "(", "}": "{" , "]": "["}
        stack = []
        for bracket in splitted:
            if len(stack) !=0 and stack[-1] == map.get(bracket, ""):
                stack.pop()
            else:
                stack.append(bracket)
        return len(stack) == 0
        

example1 = "(){[]}{"
example2 = "(([]))[]"

s = Solution()
print(s.valid_parenthesis(example1))
