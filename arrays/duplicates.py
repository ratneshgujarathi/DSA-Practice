class Solution:
    def count_duplicates(self, arr: list) -> list:
        """In an array, print the numbers that appear several times equal to their digit. For example, given the array [1, 2, 3, 3, 3, 4, 5, 5, 5, 5, 5, 6], the output would be 1, 3, and 5 because 1 appears once, 3 appears three times, and 5 appears five times."""
        el = arr[0]
        count = 0
        ans = []
        for num in arr:
            if el == num:
                count+=1
                if count == num:
                    ans.append(num)
                elif count > num and len(ans) != 0:
                    ans.pop()
            else:
                el = num
                count = 1
            
        return ans
    
    def remove_duplicates(self, arr: list) -> list:
        '''Given an integer array arr sorted in non-decreasing order, remove the duplicates in-place '''
        left, right, count = 0, 1, 0
        while right < len(arr):
            if arr[left] != arr[right]:
                arr[left+1] = arr[right]
                count+=1
                left+=1
                right+=1
            else:
                right+=1

        return arr[:count+1]
    
    def remove_duplicates_more_than_count_k(self, arr: list, k: int) -> list:
        index = 0
        el = arr[0]
        left, right, count = 0, 1, 0
        while right < len(arr):
            if arr[left] == arr[right] and count < k:
                right

            else:
                right+=1

                arr[left+2] = arr[right]
                el = arr[right]
                count+=1
                left+=1
                right+=1

            

s = Solution()
example = [1, 1, 3, 3, 3, 4, 4, 5, 5, 5, 5, 5, 6, 6]
k = 2
print(s.remove_duplicates_more_than_count_k(example, k))

