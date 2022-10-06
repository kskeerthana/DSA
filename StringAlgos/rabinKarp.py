def RabibKarp(text,pattern):
    if not pattern and text:
        return -1
    hashtext =  Hash(text,len(pattern))
    hashpattern = Hash(pattern,len(pattern))
    hashpattern.update()

    for i in range(len(text) - len(pattern) + 1):
        if hashtext.hashedValue() == hashpattern.hashedValue():
            return i
        hashtext.update()
    return -1    

class Hash:
    def __init__(self,text,pattern_size):
        self.str = text
        self.hash = 0
        for i in range(pattern_size):
            self.hash += ord(self.str[i])

        self.init = 0
        self.end = pattern_size

    def update(self):
        if self.end <= len(self.str) - 1:
            self.hash -= ord(self.str[self.init])
            self.hash += ord(self.str[self.end])
            self.init += 1
            self.end += 1

    def hashedValue(self):
        return self.hash        

print(RabibKarp('3141592653589793','16'))