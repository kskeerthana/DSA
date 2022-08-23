def SelectionSort(A):
    for i in range(len(A)-1,0,-1):
        largeValuePosition = 0
        for j in range(1,i+1):
            if A[j]>A[largeValuePosition]:
                largeValuePosition = j
        A[i],A[largeValuePosition] = A[largeValuePosition],A[i]

A =[10,4,43,5,57,91,45,9,7]
SelectionSort(A)
print(A)