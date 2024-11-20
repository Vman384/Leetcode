def findAnagrams(s: str, p: str) -> list[int]:
    i = 0
    output = []
    while i < len(s):
        for letter in p:
            if s[i] == letter:
                

print(findAnagrams( s = "cbaebabacd", p = "abc"))