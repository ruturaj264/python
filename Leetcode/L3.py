# Given a string s, return the longest 
# palindromic
 
# substring
#  in s.

 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
 

# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.

inp = 'aseiuhuiejksk'
l = len(inp)
myList = []

for i in range(l-1):
    for j in range(i+1,l):
        substr = inp[i:j]
        if substr == substr[::-1]:
            myList.append(substr)

count = list(map(len, myList))
n = count.index(max(count))
print(myList[n])