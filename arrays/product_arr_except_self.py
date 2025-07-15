class Solution:
    def product(self, arr):
        ans = [1] * len(arr)
        pref, suff = 1, 1

        for i in range(len(arr)):
            ans[i] *= pref
            pref *= arr[i]

            ans[len(arr) - 1- i] *= suff
            suff *= arr[len(arr) -1 - i]

        return ans


s = Solution()
arr = [1,2,3,4]
ans = s.product(arr)
print(ans, ans == [24, 12, 8, 6])