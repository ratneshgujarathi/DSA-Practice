from collections import Counter
class Solution:
    def sort_chars(self, strs):
        map_s = Counter(strs)
        map_s = sorted(map_s.items(), key=lambda x: -x[1])
        return "".join(chr * count for chr, count in map_s)

s = Solution()
example1 = "eert"
example2 = "Aabb"
print(s.sort_chars(example1))
print(s.sort_chars(example2))