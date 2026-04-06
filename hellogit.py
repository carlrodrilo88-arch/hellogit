number = int(input('Adivina el numero del 1 al 10: '))
date = 6

while number != date:
    if number > date:
        print('Un poco mas bajo')
        number = int(input('Adivina el numero del 1 al 10: '))
    elif number<date:
        print('Un poco mas alto')
        number = int(input('Adivina el numero del 1 al 10: '))
else:
    print('Felicidades, has adivinado el numero')