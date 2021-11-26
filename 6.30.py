import random
array = ["Samochod" , "Komputer" , "Telefon", "Portfel" , "Myszka", "Wiatrak", "Klucze", "Szklanka"]

def randelem(array):
    x=random.choice(array)
    y=random.choice(array)
    z=random.choice(array)
    a=random.choice(array)
    b=random.choice(array)
    
    print(f'{x}, {y}, {z}, {a}, {b}')
