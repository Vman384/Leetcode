reversed = []
number=121
def reverselist(number):
    for i in str(number):
        reversed.insert(0, i)
    if ''.join(reversed) == str(number):
        return True
    else:
        return False
reverselist(number)