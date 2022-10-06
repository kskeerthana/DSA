def prefixTable(pattern):
    pattern_len = len(pattern)
    k = 0 
    prefixTab = [0] * pattern_len
    for i in range(1,pattern_len):
        while k>0 and pattern[i] != pattern[k]:
            k = prefixTab[k-1]
        if pattern[i] == pattern[k]:
            k=k+1    
        prefixTab[i] = k
    print(prefixTab)    
    return prefixTab        

def kmpSearch(text,pattern):
    txt_len = len(text)
    pat_len = len(pattern)
    preTab = prefixTable(pattern)
    k = 0
    for i in range(txt_len):
        while k>0 and pattern[k] != text[i]:
            k = preTab[k-1]
        if pattern[k] == text[i]:
            k = k+1
        if k == pat_len:
            return i-pat_len+1
    return -1                

print(kmpSearch('bacbabababacaca','ababaca'))