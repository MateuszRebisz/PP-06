kolory = ["blue","yellow", "orange", "black", "white"]
f = open("kolory.txt", "a")
f.write(f'{kolory[0]}\n{kolory[1]}\n{kolory[2]}\n{kolory[3]}\n{kolory[4]}')
f.close()