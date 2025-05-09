from abc import abstractmethod


class Book:

    def __init__(self, title, author, num_of_pages, isbn, is_reserved):
        self.title = title
        self.author = author
        self.num_of_pages = num_of_pages
        self.isbn = isbn
        self.is_reserved = is_reserved

    page_material = "бумага"
    is_text_present = True

    @abstractmethod
    def print_info(self):
        pass


class FictionBook(Book):

    def print_info(self):

        if self.is_reserved:
            print(f"Название: {self.title}\n"
                  f"Автор: {self.author}\n"
                  f"Страниц: {self.num_of_pages}\n"
                  f"Материал: {self.page_material}\n"
                  f"Зарезервирована!\n")
        else:
            print(f"Название: {self.title}\n"
                  f"Автор: {self.author}\n"
                  f"Страниц: {self.num_of_pages}\n"
                  f"Материал: {self.page_material}\n")


class TextBook(Book):

    def __init__(self, title, author, num_of_pages, isbn, is_reserved, is_textbook, discipline, school_group):
        super().__init__(title, author, num_of_pages, isbn, is_reserved)

        self.is_textbook = is_textbook
        self.discipline = discipline
        self.school_group = school_group

    def print_info(self):

        if self.is_reserved:
            print(f"Название: {self.title}\n"
                  f"Автор: {self.author}\n"
                  f"Страниц: {self.num_of_pages}\n"
                  f"Предмет: {self.discipline}\n"
                  f"Класс: {self.school_group}\n"
                  f"Зарезервирована!\n")
        else:
            print(f"Название: {self.title}\n"
                  f"Автор: {self.author}\n"
                  f"Страниц: {self.num_of_pages}\n"
                  f"Предмет: {self.discipline}\n"
                  f"Класс: {self.school_group}\n")


s_king_shine = FictionBook(title="Сияние",
                           author="Стивен Кинг",
                           num_of_pages="600",
                           isbn="521-7-12345-333-1",
                           is_reserved=False)

j_abercrombie_blood_and_iron = FictionBook(title="Кровь и железо",
                                           author="Джо Аберкромби",
                                           num_of_pages="780",
                                           isbn="521-7-461776-333-1",
                                           is_reserved=False)

a_neville_ritual = FictionBook(title="Ритуал",
                               author="Адам Нэвилл",
                               num_of_pages="460",
                               isbn="521-7-324895-441-1",
                               is_reserved=False)

n_nosov_dunno_on_the_moon = FictionBook(title="Незнайка на луне",
                                        author="Николай Носов",
                                        num_of_pages="380",
                                        isbn="521-7-567934-442-1",
                                        is_reserved=False)

d_gluhovsky_metro2033 = FictionBook(title="Метро 2033",
                                    author="Дмитрий Глуховский",
                                    num_of_pages="750",
                                    isbn="521-7-876492-445-2",
                                    is_reserved=True)

makarichev_algebra_8 = TextBook(title="Алгебра 8 класс",
                                author="Юрий Макарычев",
                                num_of_pages="600",
                                isbn="521-7-428690-445-2",
                                is_reserved=True,
                                is_textbook=True,
                                discipline="Математика",
                                school_group="8")

history_of_russia_7_arsentiev = TextBook(title="История России 7 класс",
                                         author="Арсентьев Н.М.",
                                         num_of_pages="550",
                                         isbn="521-7-325098-445-2",
                                         is_reserved=False,
                                         is_textbook=True,
                                         discipline="История",
                                         school_group="7")

literature_11_michailov = TextBook(title="Литература 11 класс",
                                   author="Михайлов Олег Николаевич",
                                   num_of_pages="780",
                                   isbn="521-7-285712-445-2",
                                   is_reserved=False,
                                   is_textbook=True,
                                   discipline="Литература",
                                   school_group="11")

d_gluhovsky_metro2033.print_info()
s_king_shine.print_info()
a_neville_ritual.print_info()
n_nosov_dunno_on_the_moon.print_info()
j_abercrombie_blood_and_iron.print_info()

makarichev_algebra_8.print_info()
literature_11_michailov.print_info()
history_of_russia_7_arsentiev.print_info()
