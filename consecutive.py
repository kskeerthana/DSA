from os import remove


def removeConsec(s):
    new_string = ""
    prev = None
    for num in s:
        # if len(new_string) == 0:
        #     new_string += num
        #     prev = num
        if num != prev:
        #     continue
        
        # else:
            new_string += num
            prev = num
        # else:
        #     del     
    return new_string

print(removeConsec("156888011065"))