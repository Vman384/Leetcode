def plusOne(digits):
    num=0
    digits.reverse()
    for index,x in enumerate (digits):
        num=num+x*(10**index)
    num=num+1
    return [int(x) for x in str(num)]
print(plusOne([9,9,9,9,9,9,9,9,9,9,9]))