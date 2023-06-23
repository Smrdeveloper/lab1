def charToUpper(char):
    if len(char) > 1:
      print("Значение не строка")
      return char
    if ord('a') <= ord(char) <= ord('z'):
        return chr(ord(char) - ord('a') + ord('A'))
    else:
        return char

try:
    inputval = int(input("Выбери номер задачи(1 или 2):"))
    if inputval == 1:
        print("Задание 1")
        char = input("Введите символ:")
        char = charToUpper(char)
        print("Работа функции:", char)
    elif inputval == 2:
        print("Задание 2")
    else:
        print("Неверный ввод")
except ValueError:
    print("Неверный ввод")
