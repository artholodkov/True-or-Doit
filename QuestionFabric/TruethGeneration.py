from operator import truediv
from random import randint

def Parse(path):
    f = open(path,encoding='utf-8')
    my_list = list()
    while(True):
        line=f.readline()
        if line!="\n":
            my_list.append(line)
        if not line:
            break
    f.close()
    return my_list

def GetRandDigit (a,b):
    return randint(a,b)

def CheckRepeats(line,cash):
    if(line in cash):
        return True
    else :
        return False
        