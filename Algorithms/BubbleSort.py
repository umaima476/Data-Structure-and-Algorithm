def bubbleSort(array):
    for i in range(len(array)):
        for j in range(0, len(array)-1-i):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    return array

data = [-2, 45, 0, 11, -9]
sorted = bubbleSort(data)
print(f"Sorted Data is: {sorted}")