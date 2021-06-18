#! Python
# Программа для построения пирамиды из заданных символов, с заданными параметрами

# подключение необходимой библиотеки
import sys

# принятие данных от пользователя
Sign = str(input("Введите символ или несколько символов, из которых будет построена пирамида: "))
Choice = str(input("Как будем строить пирамиду? (1 - по длине основания; 2 - по высоте пирамиды): "))

try:
    # построение и вывод пирамиды по заданным параметрам
    if(Choice == "1"):
        NumberOfSpaces = int(input("Введите длину основания пирамиды - нечетное целое число: "))
        if(NumberOfSpaces%2 == 0):
            sys.exit()
        NumberOfSpaces = NumberOfSpaces // 2
        NumberOfSigns = 1

        print("\nРезультат: ")
        while NumberOfSpaces >= 0:
            print(" "  * len(Sign) * NumberOfSpaces + Sign * NumberOfSigns)
            NumberOfSpaces -= 1
            NumberOfSigns += 2

    if(Choice == "2"):
        NumberOfSpaces = int(input("Введите высоту пирамиды: ")) - 1
        NumberOfSigns = 1

        print("\nРезультат: ")
        while NumberOfSpaces >= 0:
            print(" " * len(Sign) * NumberOfSpaces + Sign * NumberOfSigns)
            NumberOfSpaces -= 1
            NumberOfSigns += 2


    if (Choice != "1" and Choice != "2"):
        sys.exit()

except: # обработка ошибки
    print("Ошибка! Вы ввели неверное число!", "\n")
