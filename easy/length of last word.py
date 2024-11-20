def lengthOfLastWord(s):
    s=s.split()
    lastword=s[-1]
    return len(lastword)
print(lengthOfLastWord('hello world'))