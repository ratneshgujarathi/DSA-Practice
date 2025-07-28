class Solution:
    def nextSmallerElementsRight(self, arr):
        n = len(arr)
        nse = [-1] * n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and stack[-1] > arr[i]:
                stack.pop()
            nse[i] = stack[-1] if stack else -1
            stack.append(arr[i])

        return nse 
    
    def nextSmallerElementsLeft(self, arr):
        n = len(arr)
        nse = [-1] * n
        stack = []
        for i in range(n):
            while stack and stack[-1] > arr[i]:
                stack.pop()
            nse[i] = stack[-1] if stack else -1
            stack.append(arr[i])

        return nse 
s = Solution()
arr = [4, 8, 5, 2, 25]
ans = s.nextSmallerElementsRight(arr)
print(ans, ans == [2, 5, 2, -1, -1])

ans = s.nextSmallerElementsLeft(arr)
print(ans, ans == [-1, 4, 4, -1, 2])