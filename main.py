
for iCount in range(1000):
    punkt=''
    print('1.Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.')
    print('2.Введите 10 цифр. Найду количество введенных 5')
    print('3.Вывести на экран сумму ряда чисел от 1 до 100.')
    print('4.Вывести на экран произведение ряда чисел от 1 до 10.')
    print('5.Введите число для обработки')
    print('6.Загадай число от 1 до 1000”.')
    print('  Другой символ - Завершить”.')

    punkt = input('Введите номер задачи от 1 до 6 или любой символ для завершения: ')

    if punkt == '1':
        for i in range(1,6):
            print(f'{i}. {"0"*i}')
    elif punkt == '2':
        kol=0
        for i in range(10):
            inp = input(f'Введите {i+1}-ю цифру: ')
            kol=kol+1 if inp=='5' else kol

        print(f'Введено {kol} цифр 5')
    elif punkt == '3':
        sum=0
        for i in range(1,101):
            sum+=i
        print(f'Сумма равна {sum}')
    elif punkt == '4':
        prod = 1
        for i in range(1,11):
            prod *= i
        print(f'Произведение равно {prod}')
    elif punkt == '5':
        inp = input('Введите число: ')
        # Вывести цифры числа на каждой строчке.
        for i in inp:
            print(i)

        # Найти сумму цифр числа.
        sum=0
        for i in inp:
            sum+=int(i)
        print(f'сумма цифр числа = {sum}' )

        # Найти произведение цифр числа.
        prod=1
        for i in inp:
            prod*=int(i)
        print(f'произведение цифр числа = {prod}' )

        # Дать ответ на вопрос: есть ли среди цифр числа 5?
        kol=0
        for i in inp:
            kol=kol+1 if i=='5' else kol
        have='' if kol else 'не'
        print(f'среди цифр числа {have} имеется цифра 5' )

        # Найти максимальную цифру в числе
        maxval=-1
        for i in inp:
            maxval=max(maxval,int(i))
        print(f'максимальная цифра в числе {maxval}' )

        # Найти количество цифр 5 в числе
        print(f'среди цифр числа {kol} цифр <5>' )
    elif punkt == '6':
        print("Загадайте число   от 1 до 1000")
        top=1000
        bottom=1
        found=0
        for i in range(10):
            found=int((bottom+top)/2)
            inp=input(f'Введите -1 если {found} меньше Вашего числа, 1 если больше, иначе - число угадано: ')
            if inp=='1':
                bottom=found+1
            elif inp=='-1':
                top=found-1
            else:
                print(f'Загадано {found}')
                break

    else:
        break
