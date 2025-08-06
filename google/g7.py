# grid = [
#     [0,6,0],
#     [0,0,0],
#     [0,0,0]
# ]

# grid = [
#     [0,6,0],
#     [5,8,7],
#     [0,9,0]
# ]
grid = [
    [1,0,7],
    [2,0,6],
    [3,4,5],
    [0,3,0],
    [9,0,20]
]

m = len(grid)
n = len(grid[0])
max_for_each_cell = []

temp = 0

def calc_gold(i, j, count):

    comb = [[i, j+1], [i+1, j], [i, j-1], [i-1, j]]

    for combination in comb:
        new_i, new_j = combination

        if new_j in range(n) and new_i in range(m) and grid[new_i][new_j] != 0:

            count += grid[new_i][new_j]
            temp1 = grid[new_i][new_j]
            grid[new_i][new_j] = 0

            calc_gold(new_i, new_j, count)

            grid[new_i][new_j] = temp1
            total_for_each_cell.append(count)
            count -= temp1

for i in range(m):

    for j in range(n):

        if grid[i][j] != 0: 

            temp = grid[i][j]
            grid[i][j] = 0
            total_for_each_cell = [temp]

            calc_gold(i, j, temp)

            max_for_each_cell.append(max(total_for_each_cell))
            grid[i][j] = temp

print(max(max_for_each_cell))