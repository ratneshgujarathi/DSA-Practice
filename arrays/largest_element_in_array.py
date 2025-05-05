def largest_in_array(arr: list, type: str) -> int:
    if type == "brute":
        arr.sort()
        return arr[-1]
    elif type == "optimal":
        maxi = float("-inf")
        for num in arr:
            maxi = max(maxi, num)
        return maxi
    raise Exception("Require Type of solution !!")
    

arr = [2,4,8,4,9,0,1,4,6,83,1,912,347]
ans = largest_in_array(arr, "brute")
print(f"Largest in array {arr} is {ans}")