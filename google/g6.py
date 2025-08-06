nums = [1,3,5,4,5,7,8,7]
n = len(nums)
max_subarr_len = 0
count = 1

for i in range(n-1):

    if nums[i] < nums[i+1]:
        count += 1
    else:
        if count > max_subarr_len:
            max_subarr_len = count
        count = 1

if count > max_subarr_len:
    max_subarr_len = count

print(max_subarr_len)

# for i in range(n):

#     count = 0
#     for j in range(i, n):

#         if nums[i:j+1] == sorted(nums[i:j+1]):
#             count += 1
#         else:
#             break

#     if count > max_subarr_len:
#         max_subarr_len = count