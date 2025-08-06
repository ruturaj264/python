# Given a string s, find the length of the longest substring without repeating characters.
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

from collections import Counter

inp = 'pwwkew'
l = len(inp)
myList = []

for i in range(l-1):
    for j in range(i+1,l):
        substr = inp[i:j]
        count = list(Counter(substr).values())
        if list(set(count)) == [1]:
            myList.append(len(substr))

print(max(myList))



