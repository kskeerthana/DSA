def InsertionSort(A):
    count = 0
    for i in range(1,len(A)):
        temp = A[i]
        k = i 
        while k>0 and temp< A[k-1]:
            A[k]=A[k-1]
            k -= 1
        A[k] = temp
        count += 1
        print(count)    

A =[10,4,43,5,57,91,45,9,7]
InsertionSort(A)
print(A)