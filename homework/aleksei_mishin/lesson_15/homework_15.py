# Все действия с базой данных из прошлого домашнего задания напишите с помощью Python.
#
# То есть, в этом задании вы создаете программу, которая добавляет студента,
# добавляет группу, определяет добавленного студента в только что созданную группу,
# создает в базе книги и выдает их студенту, ну и так далее
#
# Важно: никакие id не хардкодить! Хардкод - это если вы в коде пишете значение id.
# Все id нужно сохранять в переменные сразу после добавления данных в базу и потом ими пользоваться.
#
# При получении данных, распечатывайте эти данные.

from homework.aleksei_mishin.lesson_15.database_config import ST4_CONFIG
from homework.aleksei_mishin.lesson_15.request_methods import SqlRequests
from homework.aleksei_mishin.lesson_15.sql_requests import (
    ADD_STUDENT, UPDATE_STUDENT,
    ADD_BOOK, ADD_GROUP, ADD_SUBJECT,
    ADD_LESSON, ADD_MARK, GET_STUDENT_MARKS,
    GET_STUDENT_BOOKS, GET_INFO_ABOUT_STUDENT)

with SqlRequests(
        user=ST4_CONFIG["username"],
        passwd=ST4_CONFIG["password"],
        host=ST4_CONFIG["host"],
        port=ST4_CONFIG["port"],
        database=ST4_CONFIG['database']
) as sql_requests:
    student_id = sql_requests.insert_or_update_data(query=ADD_STUDENT,
                                                    data=('Жорик', 'Вартанов'))
    sql_requests.insert_or_update_data(query=ADD_BOOK,
                                       data=[
                                           ('Математический анализ', student_id),
                                           ('Математическая логига', student_id),
                                           ('Квантовая физика', student_id),
                                           ('Ядерная физика', student_id)
                                       ])
    group_id = sql_requests.insert_or_update_data(query=ADD_GROUP,
                                                  data=('Физмат', '10.2025', '06.2029'))
    sql_requests.insert_or_update_data(query=UPDATE_STUDENT,
                                       data=(group_id, student_id))
    math_subj_id, physics_subj_id = sql_requests.insert_or_update_data(query=ADD_SUBJECT,
                                                                       data=[
                                                                           ('Математика (Физмат)',),
                                                                           ('Физика (Физмат)',)
                                                                       ])
    lesson_ids_list = sql_requests.insert_or_update_data(query=ADD_LESSON,
                                                         data=[
                                                             ('Матанализ', math_subj_id),
                                                             ('Теория вероятности', math_subj_id),
                                                             ('Квантовая физика', physics_subj_id),
                                                             ('Ядерная физика', physics_subj_id)
                                                         ])

    mathan_lesson_id, prob_theory_lesson_id, quantum_phys_lesson_id, nuklear_phys_lesson_id = lesson_ids_list

    sql_requests.insert_or_update_data(query=ADD_MARK,
                                       data=[
                                           ('7', mathan_lesson_id, student_id),
                                           ('6', prob_theory_lesson_id, student_id),
                                           ('8', quantum_phys_lesson_id, student_id),
                                           ('7', nuklear_phys_lesson_id, student_id)
                                       ])
    sql_requests.get_data(query=GET_STUDENT_MARKS,
                          data=(student_id,))
    sql_requests.get_data(query=GET_STUDENT_BOOKS,
                          data=(student_id,))
    sql_requests.get_data(query=GET_INFO_ABOUT_STUDENT,
                          data=(student_id,))

    sql_requests.commit_changes()
