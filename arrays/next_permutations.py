class Solution:
    def find_partition(self, nums):
        ind = -1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                ind = 1
                break
        return ind

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start+=1
            end-=1

    def next_permutation(self, nums):
        partition = self.find_partition(nums)
        print(partition)
        for i in range(len(nums)-1, -1, -1):
            if nums[i] > nums[partition]:
                nums[i], nums[partition] = nums[partition], nums[i]
                break

        self.reverse(nums, i, len(nums)-1)

s = Solution()
arr = [1,3,4,2]
s.next_permutation(arr)
print(arr)