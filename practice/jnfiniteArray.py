# testCase = int(input())
# n = int(input())
# arr = list(map(int, input().split()))
# q = int(input())

# queries = []
# for i in range(q):
#     queries.append(list(map(int, input().split())))




array = [5,2,6,9]
l = len(array)
m = 7
n = 11
summ = 0

for i in range(m-1, n):
    summ += array[i%l]

print(summ)


# temp = []
# for i in range(total):
#     temp.append(array[i%l])

# print(temp, sum(temp[m-1:n]))


