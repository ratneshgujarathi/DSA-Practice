class Solution:
    def find_peak(self, arr: list) -> int:
        n = len(arr)
        if n == 1: return 0
        if arr[n-2] < arr[n-1]: return n - 1
        low, high = 1, n - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid] > arr[mid - 1]:
                low = mid + 1
            else: 
                high = mid - 1

        return  -1
    

s = Solution()
example = [1,2,3,1]
print(s.find_peak(example))