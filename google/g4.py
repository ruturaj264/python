blocks = [
            {
                "gym" : False,
                "school" : True,
                "store" : False
            },
            {
                "gym" : True,
                "school" : False,
                "store" : False
            },
            {
                "gym" : True,
                "school" : True,
                "store" : False
            },
            {
                "gym" : False,
                "school" : True,
                "store" : False
            },
            {
                "gym" : False,
                "school" : True,
                "store" : True
            },
]

req = ["gym", "school", "store"]
n = len(blocks)
temp = []

for i in range(n):
    
    count = 0
    temp3 = []
    for building in req:

        temp2 = []
        if blocks[i][building] != True:

            for j in range(n):

                if i != j and blocks[j][building] == True:

                    temp2.append(abs(i-j))

            temp3.append(min(temp2))

        else:
            temp3.append(0)


    temp.append(temp3)

temp4 = [max(x) for x in temp]
print(blocks[temp4.index(min(temp4))])



