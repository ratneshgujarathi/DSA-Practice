class Solution:
    def subarraySum(self, nums: list, k: int) -> int:
        pref_sum = 0
        freq = {}
        count = 0
        arrs = []
        sum_indices = {}
        for ind, num in enumerate(nums):
            pref_sum += num

            if pref_sum - k in freq:
                count+=freq[pref_sum-k]
                arrs.append(nums[sum_indices[pref_sum-k]+1: ind+1])

            freq[pref_sum] = freq.get(pref_sum, 0) + 1
            if pref_sum not in sum_indices:
                sum_indices[pref_sum] = ind

        return count, arrs
    
    
s = Solution()
arr1 = [9,4,5,2,-1,5,0,-3,8,10,-12,8,0]
arr2= [1,1,1]
k = 2
print(s.subarraySum(arr2, k))