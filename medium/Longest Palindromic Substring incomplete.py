def longestPalindrome(s: str) -> str:
    reversed = list(s)
    current = []
    max = []
    for i in range(len(s)):
        if s[i] == reversed[len(s)-1-i]:
            current.append(s[i])
        elif len(current)>0:
            if len(max)>0:
                if len(max)<len(current):
                    max.clear()
                    max = "".join(current)
                    current.clear()
                else:
                    current.clear()
            else:
                max = "".join(current)
                current.clear()
    if len(current)>0:
        if len(max)>0:
            if len(max)<len(current):
                max.clear()
                max = "".join(current)
                current.clear()
            else:
                current.clear()
        else:
            max = "".join(current)
            current.clear()
    elif len(max)<=0:
        max = s[0]


        
    return max

print(longestPalindrome('abb')) #dabab
