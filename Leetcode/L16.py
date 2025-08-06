# Given a string containing just the characters '(' and ')', return the length of the longest valid 
# (well-formed) parentheses 
# substring
# .

 

# Example 1:

# Input: s = "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()".
# Example 2:

# Input: s = ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()".
# Example 3:

# Input: s = ""
# Output: 0
 

# Constraints:

# 0 <= s.length <= 3 * 104
# s[i] is '(', or ')'.

from itertools import combinations

def checkPara(string):

    score = 0
    for letter in string:

        if letter == '(':
            score += 1
        else:
            score -= 1
        
        if score < 0:
            return False
        
    if score > 0:
        return False
    
    return True

s = ")()())"
l = len(s)
total = []

for i in range(l):
    comb = list(combinations(s, i+1))
    comb = [list(x) for x in comb]
    comb = [''.join(x) for x in comb]
    comb = list(set(comb))
    total.extend(comb)

final = max(list(map(len, list(filter(checkPara, total)))))
print(final)




    



