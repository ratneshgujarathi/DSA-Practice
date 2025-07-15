class Solution:
    def squared_arr(self, arr):
        ans = [0]*len(arr)
        left, right = 0, len(arr) - 1
        for i in range(len(ans)-1, -1, -1):
            if abs(arr[left]) > abs(arr[right]):
                ans[i] = arr[left] ** 2
                left+=1
            else:
                ans[i] = arr[right] ** 2
                right-=1

        return ans
    

s = Solution()
arr = [-4, -1, 0, 3, 6, 10]
ans = s.squared_arr(arr)
print(ans)