class Solution:
    def merge(self, arr, l, m, r):
        n1 = m - l + 1
        n2 = r - m

        left = arr[l:m + 1]
        right = arr[m + 1:r + 1]

        res = 0
        i = 0
        j = 0
        k = l
        while i < n1 and j < n2:
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
                res += (n1 - i)
            k += 1

        while i < n1:
            arr[k] = left[i]
            i += 1
            k += 1

        while j < n2:
            arr[k] = left[j]
            j += 1
            k += 1
        

        return res

    def merge_sort_with_pairs(self, arr, l, r):
        res = 0
        while l < r:
            mid = (l+r) // 2
            res += self.merge_sort_with_pairs(arr, 0, mid)
            res += self.merge_sort_with_pairs(arr, mid+1, r)

            res += self.merge(arr, l, mid, r)

        return res



    def count_inversion(self, arr):
        return self.merge_sort_with_pairs(arr, 0, len(arr) - 1)

s = Solution()
arr = [5,1,3,4,2]