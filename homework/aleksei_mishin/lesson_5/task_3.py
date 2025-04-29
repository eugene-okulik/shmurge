# Даны такие списки:
#
# students = ['Ivanov', 'Petrov', 'Sidorov']
#
# subjects = ['math', 'biology', 'geography']
#
# Распечатайте текст, который будет использовать данные из этих списков. Текст в итоге должен выглядеть так:
#
# Students Ivanov, Petrov, Sidorov study these subjects: math, biology, geography


def get_students_info(students_list: list, subjects_list: list):
    stud_str = ", ".join(students_list)
    subj_str = ", ".join(subjects_list)
    return f"Students {stud_str} study these subjects: {subj_str}"


students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

print(get_students_info(students, subjects))
