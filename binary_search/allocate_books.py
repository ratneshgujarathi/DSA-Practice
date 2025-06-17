class Solution:
    def possible(self, books, childs, pg):
        no_child, curr_page = 1, 0
        for pages in books:
            if curr_page + pages > pg:
                no_child += 1
                curr_page = 0
            curr_page += pages
        return no_child <= childs

    def findPages(self, nums, m):
        if len(nums) < m: 
            return -1
        low, high = max(nums), sum(nums)
        ans = -1

        while low <= high:
            mid = (low + high) // 2
            if self.possible(nums, m, mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans

case1 = [12, 34, 67, 90] 
m=2
s = Solution()
print(s.findPages(case1, m))