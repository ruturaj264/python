def getDivisors(num):

    div1 = []
    for i in range(2,num):
        if num % i == 0:
            div1.append(i)

    div1.append(num)

    return div1

def getSqFreeDiv(numbers):

    sqFree = []
    for div in numbers:
        root = div ** 0.5
        if root != int(root):
            sqFree.append(div)

    return sqFree


number = int(input('Number: '))

mainDiv = getDivisors(number)
mainSqFree = getSqFreeDiv(mainDiv)

print(mainDiv)
print(mainSqFree)

count = 0
finalSqFreeDiv = []
for number in mainSqFree:

    subDiv = getDivisors(number)
    subSqFree = getSqFreeDiv(subDiv)

    if subDiv == subSqFree:
        count += 1
        finalSqFreeDiv.append(number)
        
print(finalSqFreeDiv)
print(count)
