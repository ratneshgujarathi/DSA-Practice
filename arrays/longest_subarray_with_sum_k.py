class Solution:
    def longestSubarrayPos(self, arr, k):
        left, right = 0, 0
        n = len(arr)
        maxLen = 0
        s = arr[0]
        while right < n:
            while s > k and left <= right:
                s -= arr[left]
                left += 1
            if s == k:
                maxLen = max(maxLen, right - left + 1)
            s += arr[right]
            right += 1
        return maxLen, arr[left: right+1]

    def longestSubarrayNeg(self, arr, k):
        prefix_sum = 0
        sum_indices = {}
        max_length = 0
        start, end = 0, 0
        for i in range(len(arr)):
            prefix_sum += arr[i]

            if prefix_sum == k:
                max_length = i + 1
                start = 0
                end = i

            if (prefix_sum - k) in sum_indices:
                max_length = max(max_length, i - sum_indices[prefix_sum - k])
                start = sum_indices[prefix_sum - k] + 1
                end = i

            if prefix_sum not in sum_indices:
                sum_indices[prefix_sum] = i

        return max_length, arr[start: end+1]


arr1 = [5, 2, 6, 7, 0, 1, 5]
arr2 = [9, 1, -14, 2, 6, 8, 10, -12, -5]

k = 6
s = Solution()
# print(s.longestSubarrayPos(arr1, k))
print(s.longestSubarrayNeg(arr2, k))