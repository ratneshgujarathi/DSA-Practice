class Solution:
    def combination_sum(self, arr, k, i=0, curr=[], ans=[], total=0):
        if total > k:
            return
        
        if i == len(arr):
            if total == k:
                ans.append(curr[:])
            return
        
        curr.append(arr[i])
        self.combination_sum(arr,k, i+1, curr, ans, total + arr[i])
        
        curr.pop()

        self.combination_sum(arr,k, i+1, curr, ans, total)
    
        return ans

s = Solution()
print(s.combination_sum([2,3,5], 8))