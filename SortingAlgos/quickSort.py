def quickSort(arr):
    if len(arr)<2:
        return arr
    else:
        pivot = arr[0]
        lesser = [i for i in arr[1:] if i <= pivot]    
        greater = [i for i in arr[1:] if i > pivot]
        return quickSort(lesser) + [pivot] + quickSort(greater)

print(quickSort([15,10,66,12]))