class Solution:
    def find_subsets_with_sum_k(self, arr, k, i=0, curr=[], ans=[], sum=0):
        if sum > k:
            return
        
        if i == len(arr):
            if sum == k:
                ans.append(curr[:])
            return
        
        curr.append(arr[i])
        self.find_subsets_with_sum_k(arr,k, i+1, curr, ans, sum + arr[i])

        curr.pop()

        self.find_subsets_with_sum_k(arr,k, i+1, curr, ans, sum)
    
        return ans

s = Solution()
print(s.find_subsets_with_sum_k([1,2,3], 3))