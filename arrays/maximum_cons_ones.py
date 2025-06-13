class Solution:
    def max_cons_ones(self, arr: list) -> list:
        count = max_ones = 0

        for num in arr:
            if num != 0:
                count+=1
                max_ones = max(max_ones, count)
            else:
                count=0

        return max_ones
    

        
            