class Solution:
    def find_nth_nearest_root(self, num: int, root: int) -> bool:
        low, high = 1, num // root
        ans = 0
        while low <= high:
            mid = (low+high) // 2
            r_mid = 1
            for _ in range(1, root + 1):
                r_mid *=mid
                if r_mid > num:
                    break
            if r_mid <= num:
                ans = max(ans, mid)
                low = mid + 1
            else:
                high = mid - 1
        return ans
    

s = Solution()
print(s.find_nth_nearest_root(81, 3))
            