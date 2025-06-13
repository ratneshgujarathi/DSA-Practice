class Solution:
    '''Given a sorted array of nums and an integer x, write a program to find the upper bound of x. The upper bound algorithm finds the first or the smallest index in a sorted array where the value at that index is greater than a given key i.e. x. If no such index is found, return the size of the array.'''
    def upper_bound(self, arr, x):
        low = 0
        high = len(arr) - 1
        ans = len(arr)

        while low <= high:
            mid = (low+high) // 2
            if arr[mid] > x:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans

nums = [1,2,2,3]
x = 2
s = Solution()
print(s.upper_bound(nums, x))