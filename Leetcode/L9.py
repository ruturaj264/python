# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

 

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
 

# Constraints:

# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105

nums = [-1,0,1,2,-1,-4]
output = []
tempOutput = []
triplet = []
l = len(nums)

if l == 3 and sum(nums) == 0:

    output.append(nums)
    print(output)

elif l == 3 and sum(nums) != 0 or l < 3:

    print(output)

else:

    for i in range(l-2):
        for j in range(i+1, l-1):
            for k in range(j+1, l):
                if nums[i] + nums[j] + nums[k] == 0:

                    triplet.append(nums[i])
                    triplet.append(nums[j])
                    triplet.append(nums[k])

                    temp = triplet.copy()
                    temp.sort()
                    if temp not in tempOutput:
                        output.append(triplet)
                        tempOutput.append(temp)
                        triplet = []
                        temp = []

    print(output)



