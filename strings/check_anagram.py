class Solution:
    def check_anagram(self, a, b):
        if len(a) != len(b): return False
        map_a, map_b = {}, {}
        for ch_a, ch_b in zip(a, b):
            map_a[ch_a] = map_a.get(ch_a, 0) + 1
            map_b[ch_b] = map_b.get(ch_b, 0) + 1

        for key in map_a:
            if map_a[key] != map_b.get(key, 0):
                return False
            
        return True
    

s = Solution()
a = "anagram"
b = "nagaram"
print(s.check_anagram(a, b))