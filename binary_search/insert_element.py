class Solution:
    '''Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

    You must write an algorithm with O(log n) runtime complexity.

    '''
    def insert_element(self, arr, x):
        low = 0
        high = len(arr) - 1
        ans = len(arr)

        while low <= high:
            mid = (low+high) // 2
            if arr[mid] >= x:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans

nums = [1,2,2,3]
x = 2
s = Solution()
print(s.lower_bound(nums, x))