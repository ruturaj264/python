s = 'dsahjpjauf'
words = ['ahjpjau', 'ja', 'ahbwzgqnuk', 'tmnlanowax']

output = 0

for word in words:
    count = 0
    m = 0
    l = 0

    for letter1 in word:
        n = len(word)

        for i in range(m, len(s)):
            letter2 = s[i]

            if letter1 == letter2:
                count += 1
                m = i+1
                break

        if m == l:
            break

        l = m

    if count == len(word):
        output += 1

print(output)
