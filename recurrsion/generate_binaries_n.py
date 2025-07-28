class Solution:
    def generate(self, n):
        ans = []
        def backtrack(cur_bit, curr):
            if cur_bit == n:
                if curr:
                    stri = "".join(map(str, curr))
                    ans.append(stri)
                return

            curr.append(0)
            backtrack(cur_bit + 1, curr)
            curr.pop()

            curr.append(1)
            backtrack(cur_bit + 1, curr)
            curr.pop()

        backtrack(0, [])
        return ans
    

s = Solution()
ans = s.generate(2)
print(ans)