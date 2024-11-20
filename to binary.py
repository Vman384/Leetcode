a="11"
b="1"
def main(a,b):
    return bin(int(a,2)+int(b,2))[2:]
print(main(a,b))