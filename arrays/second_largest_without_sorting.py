class Solution:
    def second_largest(self, arr: list) -> int:
        largest = float('-inf')
        second_largest = float('-inf')

        for i in arr:
            if i > second_largest and i < largest:
                second_largest = i
            elif i > largest:
                second_largest = largest
                largest = i
        return second_largest
    


s = Solution()
example = [2,4,3,5,8]
example2 = [1,1,3,6,4,3,2]

print(s.second_largest(example2))