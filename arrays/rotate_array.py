class Solution:
    def reverse_inplace(self, arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end] , arr[start]
            start+=1
            end-=1

    def left_rotate_array(self, arr: list, k: int):
        k = k % len(arr)
        self.reverse_inplace(arr, 0, len(arr) - k - 1)
        self.reverse_inplace(arr, len(arr) - k, len(arr) - 1)
        self.reverse_inplace(arr, 0, len(arr) - 1)

    def right_rotate_array(self, arr: list, k: int):
        k = len(arr) - (k % len(arr))
        self.reverse_inplace(arr, 0, len(arr) - k - 1)
        self.reverse_inplace(arr, len(arr) - k, len(arr) - 1)
        self.reverse_inplace(arr, 0, len(arr) - 1)
    
s = Solution()
example = [1,2,3,4,5]
k = 2
s.right_rotate_array(example,k)
print(example)
