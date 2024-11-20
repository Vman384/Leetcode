def main(roman):
    roman = roman.upper().strip()
    roman = list(roman)
    roman.append('A')
    keys = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'A': 0}
    result = 0
    i = 0
    while i < len(roman):
        try:
            if keys[roman[i]] < keys[roman[i + 1]]:
                result = result - keys[roman[i]] + keys[roman[i + 1]]
                i = i + 2
            else:
                result = result + keys[roman[i]]
                i = i + 1
        except IndexError:
            break
    print(result)
main('i')