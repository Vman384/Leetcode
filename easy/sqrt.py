def mySqrt(x: int) -> int:
    if x == 0 or x == 1:
        return x
    start = 1
    end = x+1
    mid = (start + end)//2
    while  start < end-1:
        mid = (start + end)//2
        if mid*mid < x:
            start = mid
        elif mid*mid > x:
            end = mid
        elif mid*mid == x:
            return mid
    return start

print(mySqrt(8))