class Solution:
    def no_of_times_rotated(self, arr: list) -> int:
        low, high = 0, len(arr) - 1
        ans = arr[0]
        index = 0
        while low <= high:
            mid = (low + high) // 2
            if arr[low] <= arr[high]:
                if arr[low] < ans:
                     ans = arr[low]
                     index = low
                break
            if arr[low] <= arr[mid]:
                if arr[low] < ans:
                     ans = arr[low]
                     index = low
                low = mid + 1
            else:
                if arr[mid] < ans:
                     ans = arr[mid]
                     index = mid
                high = mid - 1

        return index

arr = [4, 5, 6, 7, 0, 1, 2, 3]
s = Solution()
print(s.no_of_times_rotated(arr))