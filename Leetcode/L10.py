# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.

 

# Example 1:

# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# Example 2:

# Input: nums = [0,0,0], target = 1
# Output: 0
# Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 

# Constraints:

# 3 <= nums.length <= 500
# -1000 <= nums[i] <= 1000
# -104 <= target <= 104

nums = [-1,2,1,-4]
comb = []
target = -5
l = len(nums)

if l == 3:

    print(sum(nums))

else:

    for i in range(l-2):
        for j in range(i+1, l-1):
            for k in range(j+1, l):

                comb.append([nums[i], nums[j], nums[k]])

    sums = [sum(x) for x in comb]
    diff = [abs(x-target) for x in sums]

    ind = diff.index(min(diff))
    print(sums[ind])
    
