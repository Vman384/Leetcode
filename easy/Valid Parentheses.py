def main(s):
    i=0
    if len(s)%2!=0:
        return False
    while i <  len(s) - 1:
        x = False
        if s[i] == '(':
            if s[i + 1] == ')':
                i+=2
                x=True
            elif s[-(i+1)]==')':
                i += 1
                x = True
            else:
                return False
        elif s[i] == '{':
            if s[i + 1] == '}':
                i+=2
                x= True
            elif s[-(i+1)]=='}':
                i+=1
                x= True
            else:
                return False
        elif s[i] == '[':
            if s[i + 1] == ']':
                i += 2
                x= True
            elif s[-(i+1)]==']':
                i += 1
                x = True
            else:
                return False
        else:
            x = False
            return x
    return x


s = '([]'
print(main(s))

def bettersolution(s):
    if len(s) < 2:
        return False
    stack=[]
    dict={'(':')','[':']','{':'}'}
    for i in s:
        if i in dict.keys():
            stack.append(i)
        else:
            if stack==[]:
                return False
            x=stack.pop()
            if i!=dict[x]:
                return False
        if stack!=[]:
            return False
    return stack==[]

print(bettersolution(s))