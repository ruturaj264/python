# colours = [1,2]
# queries = [[0,3]]
colours = [1,1,2,1,3,2,2,3,3]
queries = [[1,3], [2,2], [6,1]]

def calc_distance(colours, queries):

    n = len(colours)
    res = []
    for i, c in queries:

        count = 0
        if i == c:
            res.append(count)
        else:

            found = False
            max_distance = max(i+1, (n-i))
            for j in range(1, max_distance):

                count += 1
                next_colour = -1
                prev_colour = -1

                if i+j < n:
                    next_colour = colours[i+j]

                if i-j >= 0:
                    prev_colour = colours[i-j]

                if next_colour == c or prev_colour == c:
                    res.append(count)
                    found = True
                    break

            if not found:
                res.append(-1)

    return res

print(calc_distance(colours, queries))