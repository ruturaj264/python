# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]

from itertools import permutations

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


n = 3

a = n * '()'
perm = list(permutations(a))
perm = [list(x) for x in perm]
perm = [''.join(x) for x in perm]
perm = list(set(perm))

final = list(filter(checkPara, perm))
print(final)