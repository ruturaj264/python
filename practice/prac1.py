flower = [1,0,0,0,1,0,0,0,0,0,0,1,0,0,1]
n = 3
l = len(flower)


def check_flower_plants(n):

    for i in range(l):

        if flower[i] == 0:

            prev_space = 0
            next_space = 0

            if i - 1 >= 0:
                prev_space = flower[i-1]

            if i + 1 < l:
                next_space = flower[i+1]

            if prev_space == next_space == 0:
                flower[i] = 1
                n -= 1
                if n == 0:
                    return True
        
    return False 


print(check_flower_plants(n))


    
    
