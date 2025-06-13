class Solution:
    ''' return the nearest possible square root of any integer'''
    def sqrt(self, x):
        low, high = 1 , x
        ans = 0
        while low <= high:
            mid = (low+high) // 2
            if mid * mid <= x:
                ans = max(ans, mid)
                low = mid + 1
            else:
                high = mid - 1

        return ans


s = Solution()
print(s.sqrt(17)) 