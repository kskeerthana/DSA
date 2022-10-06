def radixSort(arr):
    radix = 10
    place_value = 1
    max_length = False
    while not max_length:
        max_length = True
        buckets =  [list() for _ in range(radix)]
        for i in arr:
            tmp = int(i/place_value)
            buckets[tmp % radix].append(i)
            
            if max_length and tmp > 0:
                max_length = False
        x = 0
        for b in range(radix):
            bucks = buckets[b]
            for i in bucks:
                arr[x] = i
                x +=1

        place_value *= radix
    return arr     

A = [534,246,933,127,277,321,454,565,220]
print(radixSort(A))                       