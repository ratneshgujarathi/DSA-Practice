
class Solution:
    '''Given a sorted array nums and an integer x. Find the floor and ceil of x in nums. The floor of x is the largest element in the array which is smaller than or equal to x. The ceiling of x is the smallest element in the array greater than or equal to x. If no floor or ceil exists, output -1.'''
    def ciel(self, arr, x):
        low, high, ans = 0, len(arr) - 1, -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] >= x:
                ans = arr[mid]
                high = mid - 1
            else:
                low = mid + 1
        return ans
    
    def floor(self, arr, x):
        low, high, ans = 0, len(arr) - 1, -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] <= x:
                ans = arr[mid]
                low = mid + 1
            else:
                high = mid - 1
        return ans
    
    def floor_ceil(self, arr, x):
        ciel = self.ciel(arr, x)
        floor = self.floor(arr, x)
        return floor, ciel


s = Solution()
example = [3, 4, 4, 7, 8, 10]
x= 5
print(s.floor_ceil(example, x))