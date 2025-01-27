def similarTextSubstringCount(key: str, text: str) -> int:
    res = 0
    key_len = len(key)

    for i in range(len(text) - key_len + 1):
      word = list(text[i:i +key_len])
      keyword = list(key)

      if word == keyword:
        res += 1
        continue

      for w in range(key_len - 1):
        word[w],word[w+1] = word[w+1],word[w]

        if word == keyword:
          res += 1
          break 

        else:
          word[w],word[w+1] = word[w+1],word[w] #swapping back
          
    return res

print(similarTextSubstringCount("mnoo","monomon"))