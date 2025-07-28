class Solution:
    def nextGreaterElementsRight(self, arr):
        n = len(arr)
        nse = [-1] * n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and stack[-1] <= arr[i]:
                stack.pop()
            nse[i] = stack[-1] if stack else -1
            stack.append(arr[i])

        return nse 
    
    def nextGreaterElementsLeft(self, arr):
        n = len(arr)
        nse = [-1] * n
        stack = []
        for i in range(n):
            while stack and stack[-1] <= arr[i]:
                stack.pop()
            nse[i] = stack[-1] if stack else -1
            stack.append(arr[i])

        return nse 
    
    def nextGreaterElementsRightCircular(self, arr):
        n = len(arr)
        nse = [-1] * n
        stack = []
        for i in range(2*n-1, -1, -1):
            index = i % n
            while stack and stack[-1] <= arr[index]:
                stack.pop()
            if i < n:
                nse[index] = stack[-1] if stack else -1
            stack.append(arr[index])

        return nse 
    
    def nextGreaterElementsLeftCircular(self, arr):
        n = len(arr)
        res = [-1] * n
        stack = []
        for i in range(2 * n):
            index = i % n
            while stack and stack[-1] <= arr[index]:
                stack.pop()
            
            res[index] = stack[-1] if stack else -1
            stack.append(arr[index])
        return res
    
s = Solution()
arr = [4, 8, 5, 2, 25]
ans = s.nextGreaterElementsRight(arr)
print(ans, ans == [8, 25, 25, 25, -1])

ans = s.nextGreaterElementsLeft(arr)
print(ans, ans == [-1, -1, 8, 5, -1])

ans = s.nextGreaterElementsLeftCircular([1,2,3,4,3])
print(ans, ans == [3, 3, 4, -1, 4])

ans = s.nextGreaterElementsRightCircular([1,2,3,4,3])
print(ans, ans == [2, 3, 4, -1, 4])