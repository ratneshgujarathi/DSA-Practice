class Solution:
    def check_sorted(self, arr: list) -> bool:
        for i in range(1, len(arr)):
            if arr[i-1] > arr[i]:
                return False
        return True
    

s = Solution()
example = [1,2,3,4,5,6]
example2 = [2,1,4,5,3]

print(s.check_sorted(example2))