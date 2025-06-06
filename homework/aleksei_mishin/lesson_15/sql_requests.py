ADD_STUDENT = "INSERT INTO students (name, second_name) VALUES (%s, %s)"
UPDATE_STUDENT = "UPDATE students SET group_id = %s WHERE id = %s"
GET_STUDENT_MARKS = "SELECT value AS mark_value FROM marks m WHERE m.student_id = %s"
GET_STUDENT_BOOKS = "SELECT title AS book_title FROM books b WHERE b.taken_by_student_id  = %s"
GET_INFO_ABOUT_STUDENT = '''SELECT
                            name,
                            second_name,
                            GROUP_CONCAT(b.title) AS book_titles,
                            g.title AS group_title,
                            l.title AS lesson_title,
                            sub.title AS subject_title,
                            m.value AS mark_value
                            FROM students s
                            JOIN books b ON s.id = b.taken_by_student_id
                            JOIN `groups` g ON s.group_id = g.id
                            JOIN marks m ON s.id = m.student_id
                            JOIN lessons l ON m.lesson_id = l.id
                            JOIN subjets sub ON l.subject_id = sub.id
                            WHERE s.id = %s
                            GROUP BY
                            s.id, g.title, m.value, l.title, sub.title'''

ADD_BOOK = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"

ADD_GROUP = "INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)"

ADD_SUBJECT = "INSERT INTO subjets (title) VALUES (%s)"

ADD_LESSON = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"

ADD_MARK = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
