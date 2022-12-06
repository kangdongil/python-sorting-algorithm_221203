def InsertionSort(list):
    for i in range(1, len(list)):
        j = i - 1
        nx_element = list[i]
        while (list[j] > nx_element) and (j >= 0):
            list[j+1] = list[j]
            j = j - 1
        list[j+1] = nx_element
    return list

list = [25, 26, 22, 24, 27, 23, 21]
InsertionSort(list)
print(list)