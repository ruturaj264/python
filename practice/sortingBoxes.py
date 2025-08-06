# n, p = list(map(int, input().split()))
# boxes = list(map(int, input().split()))

n = 5
p = 2

boxes = [20,50,30,80,70]
boxes = [20,80,30,50,70]
idealBoxes = boxes
idealBoxes.sort()

heavyBox = max(idealBoxes)
idealBoxes.remove(heavyBox)
idealBoxes.insert((p-1), heavyBox)

print(idealBoxes)
