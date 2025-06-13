class Solution:
    def min_in_sorted_rotated(self, arr: list) -> int:
        low, high = 0, len(arr) - 1
        ans = arr[0]
        while low <= high:
            mid = (low + high) // 2
            if arr[low] <= arr[high]:
                ans = min(ans, arr[low])
                break
            if arr[low] <= arr[mid]:
                ans = min(ans, arr[low])
                low = mid + 1
            else:
                ans = min(ans, arr[mid])
                high = mid - 1

        return ans
    
    def min_in_sorted_rotated_with_duplicates(self, arr: list) -> int:
        low, high = 0, len(arr) - 1
        ans = arr[0]
        while low <= high:
            mid = (low + high) // 2
            if arr[low] == arr[mid] and arr[mid] == arr[high]:
                ans = min(ans, arr[low])
                low+=1
                high-=1
                continue
            if arr[low] <= arr[mid]:
                ans = min(ans, arr[low])
                low = mid + 1
            else:
                ans = min(ans, arr[mid])
                high = mid - 1

        return ans
    

example = [3,1]
s= Solution()
print(s.min_in_sorted_rotated_with_duplicates(example))