class Solution:
    def find_subsequences(self, arr):
        ans = []
        def backtrack(ind, curr):
            if ind >= len(arr):
                if curr:
                    ans.append(curr[:])
                return
            
            curr.append(arr[ind])
            backtrack(ind + 1, curr)

            curr.pop()

            backtrack(ind + 1, curr)
        backtrack(0, [])
        return ans

s = Solution()
arr = [1,2,3]
ans = s.find_subsequences(arr)
print(ans)