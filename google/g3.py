image = [[1,0,0,0,0,0], 
         [0,1,0,1,1,1],  
         [0,0,1,0,1,0],
         [1,1,0,0,1,0],
         [1,0,1,1,0,0],
         [1,0,0,0,0,1]]

m = len(image)
n = len(image[0])

def check_border_connection(i, j):
              
    if j+1 < n and image[i][j+1] == 1:
        image[i][j+1] = 2
        check_border_connection(i, j+1)

    if i+1 < m and image[i+1][j] == 1:
        image[i+1][j] = 2
        check_border_connection(i+1, j)

    if j-1 > 0 and image[i][j-1] == 1:
        image[i][j-1] = 2
        check_border_connection(i, j-1)

    if i-1 > 0 and image[i-1][j] == 1:
        image[i-1][j] = 2
        check_border_connection(i-1, j)

for i in range(m):
    
        if i in (0, m-1):

            for j in range(n):
                 
                if image[i][j] == 1:  
                    image[i][j] = 2
                    check_border_connection(i, j)
        else:
             
            if image[i][0] == 1:
                image[i][0] = 2
                check_border_connection(i, 0)  

            elif image[i][n-1] == 1:
                image[i][n-1] = 2
                check_border_connection(i, n-1)  
    
for i in range(m):
    for j in range(n):

        if image[i][j] > 0:
           image[i][j] -= 1


for i in range(m):
    print(image[i]) 


# for i in range(m):
    
#     for j in range(n):

#         if image[i][j] == 1 and image[i][j] == 1:
            
#             image[i][j] = 0

#             if check_border_connection(i, j):
#                 image[i][j] = 1

# print(image)

# def check_border_connection(i, j):

#     result = []

#     if i in (0, m-1) or j in (0, n-1):
#         return True
#     else:

#         if image[i][j+1] == 1:

#             image[i][j+1] = 0
#             result.append(check_border_connection(i, j+1))
#             if True in result:
#                 image[i][j+1] = 1

#         if image[i+1][j] == 1 and True not in result:

#             image[i+1][j] = 0
#             result.append(check_border_connection(i+1, j))
#             if True in result:
#                 image[i+1][j] = 1

#         if image[i][j-1] == 1 and True not in result:

#             image[i][j-1] = 0
#             result.append(check_border_connection(i, j-1))
#             if True in result:
#                 image[i][j-1] = 1

#         if image[i-1][j] == 1 and True not in result:

#             image[i-1][j] = 0
#             result.append(check_border_connection(i-1, j))
#             if True in result:
#                 image[i-1][j] = 1
        
#         if True in result:
#             return True

#     return False
