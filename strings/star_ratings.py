class Solution:
    def start_rating(self,rating_str: str) -> str:
        rating = float(rating_str)
        full = int(rating)
        half = 1 if rating - full > 0 else 0
        empty = 5 - full - half

        result = ["full"] * full + ["half"] * half + ["empty"] * empty
        return " ".join(result)
    
    
    

s = Solution()
print(s.start_rating('4.8'))
