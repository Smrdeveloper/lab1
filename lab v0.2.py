try:
    inputval = int(input("Выбери номер задачи(1 или 2):"))
    if inputval == 1:
        print("Задание 1")
    elif inputval == 2:
        print("Задание 2")
    else:
        print("Неверный ввод")
except ValueError:
    print("Неверный ввод")
