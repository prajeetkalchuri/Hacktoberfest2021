import math 
from math import *
def encryption(s):
    #s.strip()
    L = len(s)
    row = floor(sqrt(L))
    column = ceil(sqrt(L))
    #print(row)
    #print(column)
    
    result = []
    
    #to iterate the columns 
    for i in range (column):
        temp = []
        j = 0
        while i+j < L:
            temp.append(s[i+j])
            #incrementing by c means we will go to the next row 
            j += column
            #store temp result to final result 
        result.append("".join(temp))
        
    #finally we will have to return the result will space in between 
    
    return " ".join(result)
    
    
    
    
    
s = 'feedthedog'

print(encryption(s))

#2nd Approach 
"""
def encryption(s):
    s = ''.join(s.split())
    L = len(s)
    sq_L = math.sqrt(L)
    row = math.floor(sq_L)
    column = math.ceil(sq_L)
    
    if row*column < L:
        row += 1
        
    i = 0
    arr = []
    
    for x in range(row):
        temp = []
        for c in range(column):
            if i < L:
                temp.append(s[i])
                i += 1
            else :
                temp.append('')
        arr.append(temp)
        
    result = []
    
    for y in range(column):
        temp = []
        for r in range(row):
            temp.append(arr[r][y])
        result.append(''.join(temp))
    return (' '.join(result))





    
s = 'feedthedog'

print(encryption(s))
"""
