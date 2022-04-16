def heapSort(A):
    length = len(A)
    leastParent = length//2
    for i in range(leastParent -1 ,-1,-1):
        heapify(A,length,i)

    for i in range(length -1 ,0,-1):
        A[i],A[0] =A[0],A[i] 
        heapify(A,i,0)

def heapify(A,n,i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2
    
    if left < n and A[largest]<A[left]:
        largest = left
    if right < n  and A[largest] < A[right]:
        largest = right
    if largest != i:
        A[i],A[largest] = A[largest],A[i]
        heapify(A,n,largest)

A = [12, 11, 13, 5, 6, 7]
heapSort(A)
n = len(A)
print("Sorted array is")
for i in range(n):
    print("%d " % A[i], end='')
