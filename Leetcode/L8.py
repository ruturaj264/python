# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters if it is non-empty.

inp = ["flower","flow","flowing"]
valid = []
m = min(list(map(len, inp)))

if list(set(inp))[0] == inp[0]:

    print(inp[0])

else:

    for i in range(m):
        
        substr = inp[0][:i+1]
        list1 = list(filter(lambda x:(x[:i+1]==substr), inp))

        if inp == list1:
            valid.append(substr)
        else:
            break


if len(valid) > 0:
    print(valid[-1])
else:
    print(' ')