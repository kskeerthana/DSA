import math

def insertionSort(A):
    for i in range(1,len(A)):
        temp = A[i]
        k = i 
        while k>0 and temp< A[k-1]:
            A[k]=A[k-1]
            k -= 1
        A[k] = temp

def bucketSort(A):
    code = Hashing(A)
    buckets = [list() for _ in range(code[1])]
    for i in A:
        x = reHashing(i,code)
        buck = buckets[x]
        buck.append(i)
    for bucket in buckets:
        insertionSort(bucket)
    ndx = 0
    for b in range(len(buckets)):
        for v in buckets[b]:
            A[ndx] = v
            ndx += 1
    return A               

def Hashing(A):
    m = A[0]
    for i in range(1,len(A)):
        if m < A[i]:
            m = A[i]
    result = [m,int(math.sqrt(len(A)))]
    return result

def reHashing(i,code):
    return int(i/code[0]*(code[1]-1))



