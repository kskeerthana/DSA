def countingSort(arr,k):
    b = [0 for i in arr]
    c = [0 for i in range(0,k+1)]

    for i in range(0,len(arr)):
        c[arr[i]] +=1

    for i in range(1,k+1):
        c[i] += c[i-1]

    for i in range(len(arr)-1,-1,-1):
        arr_temp = arr[i]
        count_temp = c[arr_temp] - 1
        b[count_temp] = arr_temp
        count_temp -=1
    return b    

arr=[534,246,933,127,277,321,454,565,220]
print(countingSort(arr,1000))