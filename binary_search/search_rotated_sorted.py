class Solution:
    '''Given an integer array nums, sorted in ascending order (with distinct values) and a target value k. The array is rotated at some pivot point that is unknown. Find the index at which k is present and if k is not present return -1.'''
    def search(self, arr: list, target: int) -> int:
        low, high = 0 , len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                return mid
            if arr[low] <= arr[mid]:
                if arr[low] <= target and target <= arr[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if target >= arr[mid] and  target <= arr[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return  -1
    
    def search_with_duplicates(self, arr: list, target: int) -> bool:
        low, high = 0 , len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                return True
            if arr[low] == arr[mid] and arr[mid] == arr[high]:
                low+=1
                high-=1
                continue

            if arr[low] <= arr[mid]:
                if arr[low] <= target and target <= arr[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if target >= arr[mid] and  target <= arr[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return  False


s = Solution()
example = [2,5,6,0,0,1,2]
k = 0
print(s.search_with_duplicates(example, k))
