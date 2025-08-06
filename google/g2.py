total_land = [[0,1,1,0,1], 
              [1,1,0,1,0],
              [0,1,1,1,0],
              [1,1,1,1,0],
              [1,1,1,1,1],
              [0,0,0,0,0]]

n = len(total_land)
m = len(total_land[0])
land_index = -1
temp = []

for land in total_land:
    land_index += 1
    number_index = -1

    for number in land:
        number_index += 1

        if number == 1:
            max_square = min(m-number_index, n-land_index)

            for i in range(max_square):
                count = 0

                for j in range(i+1):

                    temp_land = total_land[land_index+j]
                    count += sum(temp_land[number_index:number_index+i+1])

                if count == (i + 1) ** 2:
                    temp.append(count)
                else:
                    break

print(max(temp))
