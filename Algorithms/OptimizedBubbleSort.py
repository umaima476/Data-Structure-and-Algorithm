def bubbleSort(array):
    for i in range(len(array)):
        swapped = False
        for j in range(0, len(array)-1-i):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                swapped = True
        if not swapped:
            print("Given array is already sorted")
            break
    return array

data = [9, 10, -2, 45, 11]
data2 = [3, 4, 5, 6, 7]
sorted = bubbleSort(data)
print(sorted)