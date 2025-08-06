# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the 
# input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true

# Example 3:

# Input: s = "(]"

# Output: false

# Example 4:

# Input: s = "([])"

# Output: true

 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

inp = "[]({})"

round = 0
square = 0
curly = 0

for letter in inp:

    if letter == '(':
        round += 1
    elif letter == ')':
        round -= 1
    elif letter == '[':
        square += 1
    elif letter == ']':
        square -= 1
    elif letter == '{':
        curly += 1
    elif letter == '}':
        curly -= 1

if round == 0 and square == 0 and curly == 0:
    print('true')
else:
    print('false')
