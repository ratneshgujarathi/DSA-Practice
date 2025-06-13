class Solution:
    '''Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value. If the target is not found in the array, return [-1, -1].'''
    def lower_bound(self, arr, x):
        low, high = 0, len(arr) - 1
        ans = len(arr)
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] >= x:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
    
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
    

    def first_last_occurence(self, arr: list, target: int) -> list:
        lb = self.lower_bound(arr, target)
        if lb == len(arr) or arr[lb] != target:
            return [-1, -1]
        return [lb, self.upper_bound(arr, target) - 1]


s = Solution()
example = [5, 7, 7, 8, 8, 10]
target = 8
print(s.first_last_occurence(example, target))