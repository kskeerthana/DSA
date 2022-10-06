
def BruteForceSearch(text,pattern):
    if not pattern:
        return 0
    for i in range(len(text)-len(pattern)+1):
        stri = i; patterni = 0
        while stri<len(text) and patterni<len(pattern) and text[stri] == pattern[patterni]:
            stri += 1
            patterni +=1
        if patterni == len(pattern):
            print('pattern found at :',i)  
    return -1

print(BruteForceSearch('abcabcabcabcabcd','abcd'))             