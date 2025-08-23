import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class BaseElement:
    def __init__(self, browser, name, how, what):
        self.browser = browser
        self.name = name
        self.locator = how, what

    def get_element(self):
        self.is_element_visible(*self.locator)
        return self.browser.find_element(*self.locator)

    def get_elements(self):
        self.is_element_visible(*self.locator)
        return self.browser.find_elements(*self.locator)

    def get_element_by_text(self, text):
        with allure.step(f'Поиск элемента: {text}'):
            self.is_element_visible(By.XPATH, f"//*[text()='{text}']")
            element = self.browser.find_element(By.XPATH, f"//*[text()='{text}']")
        return element

    def select_element_by_text(self, text):
        with allure.step(f'Выбрать элемент: {text}'):
            self.is_element_visible(By.XPATH, f"//*[text()='{text}']")
            element = self.browser.find_element(By.XPATH, f"//*[text()='{text}']")
            element.click()

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

    def click(self, element=None):
        element = element if element else self.get_element()
        with allure.step(f"Клик по: {self.name}"):
            action = AC(self.browser)
            action.click(element)
            action.perform()

    def double_click(self, element=None):
        element = element if element else self.get_element()
        with allure.step(f"Двойной клик по: {self.name}"):
            action = AC(self.browser)
            action.double_click(element)
            action.perform()

    def submit(self, element=None):
        with allure.step('Подтвердить'):
            element = element if element else self.get_element()
            with allure.step(f"Подтвердить ввод в {self.name}"):
                element.submit()

    def scroll_to_element(self, element=None):
        element = element if element else self.get_element()
        action = AC(self.browser)
        action.scroll_to_element(element)
        action.perform()

    def move_to_element(self, element=None):
        element = element if element else self.get_element()
        action = AC(self.browser)
        action.move_to_element(element)
        action.perform()

    def get_text_of_element(self):

        return self.get_element().text


class Button(BaseElement):
    pass


class Input(BaseElement):

    def clear_input(self):
        action = AC(self.browser)
        input_1 = self.get_element()
        input_value = input_1.get_attribute("value")
        with allure.step(f"Очистить: {self.name}"):
            while len(input_value) > 0:
                action.double_click(input_1)
                action.send_keys_to_element(input_1, Keys.BACKSPACE).perform()
                input_value = input_1.get_attribute("value")

    def fill_input(self, data):
        action = AC(self.browser)
        input_1 = self.get_element()
        with allure.step(f"Ввод данных в {self.name}"):
            action.click(input_1)
            action.send_keys_to_element(input_1, data).perform()
        input_1_value = input_1.get_attribute("value")
        with allure.step(f"Проверка введенных данный в {self.name}"):
            assert input_1_value == data, f'Некорректные данные в инпуте! ОР: {data}, ФР: {input_1_value}'

        return data

    def fill_autocomplete_input(self, data):
        action = AC(self.browser)
        input_1 = self.get_element()
        with allure.step(f"Ввод данных в инпут {self.name} с автозаполнением"):
            action.click(input_1)
            action.send_keys_to_element(input_1, data)
            action.send_keys_to_element(input_1, Keys.ENTER).perform()

        return data


class Selector(BaseElement):

    def select_by_text(self, text: str):
        with allure.step(f'В дропдауне выбрать: {text}'):
            dropdown = Select(self.get_element())
            dropdown.select_by_visible_text(text)

        return text


class Table(BaseElement):

    def return_data(self):
        table = self.get_element()

        data = {}
        rows = table.find_elements(By.TAG_NAME, "tr")
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            row_data = [cell.text.strip() for cell in cells]
            if row_data:
                data[row_data[0]] = row_data[1:]

        return data
