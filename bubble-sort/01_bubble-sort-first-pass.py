list = [25, 21, 22, 24, 23, 27, 26]

lastElementIndex = len(list) - 1
print(0, list)
for idx in range(lastElementIndex):
    if list[idx] > list[idx+1]:
        list[idx], list[idx+1] = list[idx+1], list[idx]
    print(idx+1, list)