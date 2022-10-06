d=256
def rabinKarp(text,pattern,q):
    pat_size = len(pattern)
    text_size = len(text)
    hashpat = 0
    hashtext = 0
    hashValue = 1

    for i in range(pat_size-1):
        hashValue = (hashValue%d)*q

    for i in range(pat_size):
        hashpat = (d*hashpat + ord(pattern[i]))%q  
        hashtext = (d*hashtext + ord(text[i]))%q  

    for i in range(text_size - pat_size +1):
        if hashpat == hashtext:
            for j in range(pat_size):
                if text[i+j] != pattern[j]: 
                    break
                else:
                    j+=1 
            if j == pat_size:
                print('pattern found at:',i)

        if i < text_size - pat_size:
            hashtext = (d*(hashtext - ord(text[i])*hashValue) + ord(text[i+pat_size]))%q  

            if hashtext<0:
                hashtext =  hashtext+q

txt = "GEEKS FOR GEEKS"
pat = "GEEK"
q = 101 

rabinKarp(txt,pat,q)

