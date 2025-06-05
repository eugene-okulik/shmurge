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
from homework.aleksei_mishin.lesson_15.sql_requests import SqlRequests

with SqlRequests(
        user=ST4_CONFIG["username"],
        passwd=ST4_CONFIG["password"],
        host=ST4_CONFIG["host"],
        port=ST4_CONFIG["port"],
        database=ST4_CONFIG['database']
) as sql_requests:
    student_id = sql_requests.insert_into_table(table_name='students',
                                                columns=('name', 'second_name'),
                                                values=[
                                                    ('Алексей', 'Мишин')
                                                ])

    sql_requests.insert_into_table(table_name='books',
                                   columns=('title', 'taken_by_student_id'),
                                   values=[
                                       ('Математический анализ', student_id),
                                       ('Математическая логика', student_id),
                                       ('Квантовая физика', student_id),
                                       ('Ядерная физика', student_id)
                                   ])

    group_id = sql_requests.insert_into_table(table_name='`groups`',
                                              columns=('title', 'start_date', 'end_date'),
                                              values=[
                                                  ('Физмат', '10.2025', '06.2029')
                                              ])

    sql_requests.update_data_in_table(table_name='students',
                                      set_column='group_id',
                                      set_value=group_id,
                                      where_column='id',
                                      where_value=student_id
                                      )

    math_subj_id = sql_requests.insert_into_table(table_name='subjets',
                                                  columns=('title',),
                                                  values=[
                                                      ('Математика (Физмат)',)
                                                  ])

    physics_subj_id = sql_requests.insert_into_table(table_name='subjets',
                                                     columns=('title',),
                                                     values=[
                                                         ('Физика (Физмат)',)
                                                     ])

    mathan_lesson_id = sql_requests.insert_into_table(table_name='lessons',
                                                      columns=('title', 'subject_id'),
                                                      values=[
                                                          ('Матанализ', math_subj_id)
                                                      ])

    prob_theory_lesson_id = sql_requests.insert_into_table(table_name='lessons',
                                                           columns=('title', 'subject_id'),
                                                           values=[
                                                               ('Теория вероятности', math_subj_id)
                                                           ])

    quantum_phys_lesson_id = sql_requests.insert_into_table(table_name='lessons',
                                                            columns=('title', 'subject_id'),
                                                            values=[
                                                                ('Квантовая физика', physics_subj_id)
                                                            ])

    nuklear_phys_lesson_id = sql_requests.insert_into_table(table_name='lessons',
                                                            columns=('title', 'subject_id'),
                                                            values=[
                                                                ('Ядерная физика', physics_subj_id)
                                                            ])

    sql_requests.insert_into_table(table_name='marks',
                                   columns=('value', 'lesson_id', 'student_id'),
                                   values=[
                                       ('7', mathan_lesson_id, student_id),
                                       ('6', prob_theory_lesson_id, student_id),
                                       ('8', quantum_phys_lesson_id, student_id),
                                       ('7', nuklear_phys_lesson_id, student_id)
                                   ])

    sql_requests.commit_changes()

    sql_requests.select_from_table(columns='value',
                                   table_name='marks',
                                   where_columns=('student_id',),
                                   where_values=(student_id,)
                                   )

    sql_requests.select_from_table(columns='title',
                                   table_name='books',
                                   where_columns=('taken_by_student_id',),
                                   where_values=(student_id,)
                                   )

    # Вот с этим методом я плотно припух, так и не сообразил, как сделать его хоть немного универсальным
    sql_requests.get_info_about_user(student_id=student_id)
