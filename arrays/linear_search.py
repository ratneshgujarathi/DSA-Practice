class Solution:
    def linear_search(self, arr: list, target: int) -> int:
        for i, num in enumerate(arr):
            if num == target:
                return i
        return -1
    

s =Solution()
print(s.linear_search([2,3,1,11,67,9,21,10], 67))