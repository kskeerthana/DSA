def mergeSort(arr):
    if len(arr)>1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        mergeSort(left)
        mergeSort(right)
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                arr[k] =left[i] 
                i=i+1
            else:
                arr[k] = right[j]
                j = j+1
            k = k+1     
        while i<len(left):
            arr[k] = left[i]
            i = i+1
            k=k+1
        while j<len(right):
            arr[k] = right[j]
            j = j+1
            k=k+1      
    else:
        return 0           

A= [533,246,933,127,277,321,454,565,220]
mergeSort(A)
print(A)       
            
