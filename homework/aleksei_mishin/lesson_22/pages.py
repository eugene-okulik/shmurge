import allure
import random
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from elements import Button, Input, Selector, Table
from locators import QaPractLocators, ToolsQaLocators, HerokuAppLocators
from test_data import UserTestData, OtherTestData
from time import sleep


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        with allure.step(f'Открыть страницу: {self.url}'):
            return self.browser.get(self.url)

    def is_element_visible(self, how, what, timeout=10, freq=0.5):
        try:
            WebDriverWait(self.browser, timeout, freq).until(EC.visibility_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def is_not_element_visible(self, how, what, timeout=10, freq=0.5):
        try:
            WebDriverWait(self.browser, timeout, freq).until_not(EC.visibility_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True


class InputsPage(BasePage):

    def __init__(self, browser, url):
        super().__init__(browser, url)

        self.text_input = Input(self.browser, 'Поле ввода текста', *QaPractLocators.TEXT_INPUT)
        self.language_selector = Selector(self.browser, 'Дропдаун: выбо языка', *QaPractLocators.LANGUAGE_SELECTOR)

    def text_should_be_correct(self, exp_res):
        with allure.step('Отображаемый текст соответствует введенному'):
            self.is_element_visible(*QaPractLocators.RESULT_TEXT)
            act_res = self.browser.find_element(*QaPractLocators.RESULT_TEXT).text
            assert exp_res == act_res, f"Текст не соответствует введенному!\n" \
                                       f"ОР: {exp_res}\n" \
                                       f"ФР: {act_res}"


class StudentRegistrationPage(BasePage):

    def __init__(self, browser, url):
        super().__init__(browser, url)

        self.userdata = UserTestData()
        self.registration_form = Button(self.browser, 'Форма регистрации', *ToolsQaLocators.REGISTRATION_FORM)
        self.f_name = Input(self.browser, 'Поле Имя', *ToolsQaLocators.FIRSTNAME_INPUT)
        self.l_name = Input(self.browser, 'Поле Фамилия', *ToolsQaLocators.LASTNAME_INPUT)
        self.genders = Button(self.browser, 'Радио баттон Пол', *ToolsQaLocators.GENDER)
        self.email = Input(self.browser, 'Поле Email', *ToolsQaLocators.EMAIL_INPUT)
        self.phone = Input(self.browser, 'Поле Телефон', *ToolsQaLocators.PHONE_INPUT)
        self.hobbies = Button(self.browser, 'Чекбокс Хобби', *ToolsQaLocators.HOBBIES)
        self.address = Input(self.browser, 'Поле Адрес', *ToolsQaLocators.CURRENT_ADDRESS)
        self.state_name = Button(self.browser, 'Селектор Штат', *ToolsQaLocators.STATE_SELECTOR)
        self.city_name = Button(self.browser, 'Селектор Город', *ToolsQaLocators.CITY_SELECTOR)

    def fill_registration_form(self, userdata=None):
        with allure.step('Заполнение формы регистрации'):
            userdata = userdata if userdata else self.userdata
            state = random.choice(list(userdata.location.keys()))
            city = random.choice(userdata.location[state])

            self.f_name.fill_input(userdata.firstname)
            self.l_name.fill_input(userdata.lastname)
            self.genders.click(self.genders.get_element_by_text(userdata.gender))
            self.email.fill_input(userdata.email)
            self.phone.fill_input(userdata.phone)
            self.set_birthday(userdata.birthday_day, userdata.birthday_month, userdata.birthday_year)
            self.set_subjects(['Maths', 'Arts'])
            self.set_hobbies(['Sports', 'Reading', 'Music'])
            self.address.scroll_to_element()
            self.address.fill_input(self.userdata.address)
            self.set_location(state, city)

    def set_birthday(self, day: str, month: str, year: str):
        with allure.step('Ввод даты рождения'):
            if day[0] == '0':
                day = day[1]
            birthday_input = Input(self.browser, 'Поле Дата рождения', *ToolsQaLocators.BIRTHDAY_INPUT)
            month_selector = Selector(self.browser, 'Дропдаун Месяц', *ToolsQaLocators.MONTH_SELECTOR)
            year_selector = Selector(self.browser, 'Дропдайн Год', *ToolsQaLocators.YEAR_SELECTOR)
            birthday_input.click()
            month_selector.select_by_text(month)
            year_selector.select_by_text(year)
            day = Button(self.browser, 'День', *ToolsQaLocators().select_day(day))
            day.click()

    def set_subjects(self, data: list):
        with allure.step('Ввод учебных дисциплин'):
            input_1 = Input(self.browser, 'Поле Предметы', *ToolsQaLocators.SUBJECTS)
            for subj in data:
                input_1.fill_autocomplete_input(subj)

    def set_hobbies(self, data: list):
        with allure.step('Выбор хобби'):
            for d in data:
                checkbox = self.hobbies.get_element_by_text(d)
                checkbox.click()

    def set_location(self, state, city):
        with allure.step('Выбор локации'):
            self.state_name.click()
            self.state_name.select_element_by_text(state)
            self.city_name.click()
            self.city_name.select_element_by_text(city)

    def print_result(self):
        with allure.step('Распечатать данные из таблицы с результатом'):
            table = Table(self.browser, 'Таблица с результатом', *ToolsQaLocators.RESULT_TABLE)
            data_dict = table.return_data()
            print()
            for k, v in data_dict.items():
                print(f"{k}: {v}")


class HerokuAppPage(BasePage):

    def __init__(self, browser, url):
        super().__init__(browser, url)

        self.start_button = Button(self.browser, 'Кнопка: Старт', *HerokuAppLocators.START_BUTTON)

    def should_be_hello_world(self):
        exp_res = 'Hello World!'
        with allure.step('Отображается текст Hello World!'):
            self.is_element_visible(*HerokuAppLocators.HELLO_WORLD)
            act_res = self.browser.find_element(*HerokuAppLocators.HELLO_WORLD).text
            assert act_res == exp_res, f'Отображается некорректный текст!\n' \
                                       f'ОР: {exp_res}\n' \
                                       f'ФР: {act_res}'
