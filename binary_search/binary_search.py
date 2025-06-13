class Solution:
    def binary_search(self, arr: list, target: int) -> int:
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid
        return -1
    
    def binary_search_recursive(self, arr: list, target: int) -> int:
        def search(low: int, high: int) -> int:
            if low > high:
                return -1
            mid = (low + high) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                return search(mid + 1, high)
            else:
                return search(low, mid - 1)
        
        return search(0, len(arr) - 1)


s = Solution()
example = [1, 2, 3, 4, 5]
print(s.binary_search_recurrsion(example, 1))
