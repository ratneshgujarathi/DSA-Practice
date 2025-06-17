import math
class Solution:
    def find_hrs(self, arr, h):
        ans = 0 
        for num in arr:
            ans += math.ceil(num/ h)
        return ans
    
    def koko_banana(self, piles, hrs):
        low, high = 0, max(piles)
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            if self.find_hrs(piles, mid) <= hrs:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans 
    
s = Solution()
piles = [30,11,23,4,20]
hrs = 5
print(s.koko_banana(piles, hrs))