array = [1,2,3,4,5,6,7,8,9,10]
even = []
odd = []
for x in array:
    if x % 2 == 0:
        even.append(x)
    else:
        odd.append(x)
        
print( even + odd ) 