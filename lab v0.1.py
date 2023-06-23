try:
    input = int(input("Выбери номер задачи(1 или 2):"))
    if input == 1:
        print("Задание 1")
    elif input == 2:
        print("Задание 2")
    else: 
        print("Неверный ввод")
except ValueError:
    print("Неверный ввод")
