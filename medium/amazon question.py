def find(input1,input2):
    count = 1
    found = input1.find(input2)
    i = 0
    while found == -1:
        count+=1
        for letter in input1:
            if letter == input2[i]:
                if i+1<len(input2):
                    i += 1
                else:
                    return count
        input1+=input1

    return count

print(find("mtle","metl"))
        