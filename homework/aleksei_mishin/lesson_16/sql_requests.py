SEARCH_STUDENT = '''SELECT
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
                    WHERE (s.name, s.second_name, g.title, b.title, sub.title, l.title, m.value) 
                    = 
                    (%s, %s, %s, %s, %s, %s, %s)
                    GROUP BY
                    s.id, g.title, m.value, l.title, sub.title'''
