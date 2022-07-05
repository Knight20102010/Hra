
import random

def hadanie(a,b):
    print(f'Myslím si číslo,medzi {a,b} uhádni ho!')   
    x = random.randint(a,b)
    for i in range(1,9):
        n = int(input('tvoj tip je: '))
        if n == x:
            print('uhádol si. Congratulation')
            break
        if n < x:
            print('pridaj')
        else:
            print('uber')
    print(f'myslel som číslo {x}')

print(hadanie(1,9))
