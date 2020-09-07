number = 21
print('Угадай загаданное число число!')
a = int(input('Введите ваше число:'))
if a == number:
    print("Вы угадали!!!")        # условие if
elif number > a:
    print('Ваше число меньше загаданного')
else:
    print('Ваше число больше загаданного')


print("Ещё раз, пока не угадаете!")
pravda = True
while pravda:
    b = int(input("Введите число: "))
    if number == b:
        print('Поздравляю, угадали!')    # ЦИКЛ while
        pravda = False
    elif number>b:
        print('Ваше число меньше загаданного')
    else:
        print('Ваше число больше загаданного')


for i in range(10):       # для i < 10 с шагом 1. Пропустит 5
    if i == 5:
        continue
    else:
        print(i)
input()