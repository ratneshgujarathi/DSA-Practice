class Solution:
    def reverse(self, arr, i = 0):
        if i >= len(arr) // 2:
            return arr
        
        arr[i], arr[len(arr)-i-1] = arr[len(arr)-i-1], arr[i]
        return self.reverse(arr, i+1)
    
s = Solution()
print(s.reverse([1,2,3,4,5]))
        
        
