INSERT INTO students (name, second_name)
VALUES ('Алексей', 'Мишин')

INSERT INTO books (title, taken_by_student_id) VALUES
('Математический анализ', 20493),
('Математическая логига', 20493),
('Квантовая физика', 20493),
('Ядерная физика', 20493)

INSERT INTO `groups` (title, start_date, end_date)
VALUES ('Физмат', '10.2025', '06.2029')

UPDATE students SET group_id = 5202 WHERE id = 20493

INSERT INTO subjets (title) VALUES
('Математика (Физмат)'),
('Физика (Физмат)')

INSERT INTO lessons (title, subject_id) VALUES
('Матанализ', 10684),
('Теория вероятности', 10684),
('Квантовая физика', 10685),
('Ядерная физика', 10685)

INSERT INTO marks (value, lesson_id, student_id) VALUES
('7', 10487, 20493),
('6', 10488, 20493),
('8', 10489, 20493),
('7', 10490, 20493)

SELECT value AS student_value
FROM marks m
WHERE m.student_id = 20493

SELECT title AS book_title
FROM books b
WHERE b.taken_by_student_id  = 20493


-- Вот тут я конкретно припух. У меня выводится по 4 книги на каждую запись.
-- Я так и не смог нормально вывести все в 4 строки. Только таким вот образом
SELECT
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
WHERE s.id = 20493
GROUP BY
s.id, g.title, m.value, l.title, sub.title
