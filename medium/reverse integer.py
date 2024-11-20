def reverse(x: int):
    negative = False
    if x<0:
        negative = True
    x = str(x)[::-1]
    if negative:
        x = x[:-1]
        x = int(x)
        x = -1*x
    x = int(x)
    if x > 2**31 - 1 or x < -2**31:
        return 0
    return x

print(reverse(123))
    