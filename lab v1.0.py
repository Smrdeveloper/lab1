def charToUpper(char):
    if len(char) > 1:
      print("Значение не строка")
      return char
    if ord('a') <= ord(char) <= ord('z'):
        return chr(ord(char) - ord('a') + ord('A'))
    else:
        return char

def bestStudent(students):
    best_student = None
    best_average_grade = 0
    
    for student in students:
        total_grade = 0
        num_grades = 0
        
        for exam in student['exams']:
            total_grade += exam['grade']
            num_grades += 1
        
        if num_grades > 0:
            average_grade = total_grade / num_grades
            
            if average_grade > best_average_grade:
                best_student = student
                best_average_grade = average_grade
    
    if best_student is not None:
        print(f"ФИО: {best_student['name']}")
        print("Предметы и оценки:")
        for exam in best_student['exams']:
            print(f"{exam['subject']}: {exam['grade']}")
    else:
        print("Список студентов пустой")

students = [
    {
        'name': 'Иванов Иван',
        'birthday': (2000, 1, 1),
        'exams': [
            {'subject': 'Математика', 'date': '01.02.2022', 'grade': 4},
            {'subject': 'Физика', 'date': '05.02.2022', 'grade': 5},
            {'subject': 'Программирование', 'date': '10.02.2022', 'grade': 5},
        ]
    },
    {
        'name': 'Петров Петр',
        'birthday': (2001, 2, 2),
        'exams': [
            {'subject': 'Математика', 'date': '01.02.2022', 'grade': 5},
            {'subject': 'Физика', 'date': '05.02.2022', 'grade': 4},
            {'subject': 'Программирование', 'date': '10.02.2022', 'grade': 4},
        ]
    },
    {
        'name': 'Сидоров Сидор',
        'birthday': (2002, 3, 3),
        'exams': [
            {'subject': 'Математика', 'date': '01.02.2022', 'grade': 3},
            {'subject': 'Физика', 'date': '05.02.2022', 'grade': 3},
            {'subject': 'Программирование', 'date': '10.02.2022', 'grade': 4},
        ]
    }
]

try:
    inputval = int(input("Выбери номер задачи(1 или 2):"))
    if inputval == 1:
        print("Задание 1")
        char = input("Введите символ:")
        char = charToUpper(char)
        print("Работа функции:", char)
    elif inputval == 2:
        print("Задание 2")
        bestStudent(students)
    else:
        print("Неверный ввод")
except ValueError:
    print("Неверный ввод")
