class Solution:
    def find_subsets(self, arr, i=0, curr=[], ans=[]):
        if i == len(arr):
            ans.append(curr[:])
            return 
        
        curr.append(arr[i])
        self.find_subsets(arr, i+1, curr, ans)

        curr.pop()

        self.find_subsets(arr, i+1, curr, ans)
    
        return ans

s = Solution()
print(s.find_subsets([1,2,3]))