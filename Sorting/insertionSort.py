#insertion sort   O(n) = n**2
def insertionSort(arr):
    for i in range(0, len(arr)):
        key = arr[i]
        for j in range(i, 0, -1):
            if(key < arr[j-1]):
                arr[j] = arr[j-1]
                arr[j-1] = key
    return arr

#driver code for testing
print(insertionSort([1,3,5,0,1.3,-0.5,1,-2,5]))