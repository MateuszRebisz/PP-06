tablica = [4,2,7,3,6,9,6,4.5,3.5,5.5,9,7,5]

x = float(input(f'Your Number: '))
for y in tablica:
    if x > y:
        print(y,end=",")