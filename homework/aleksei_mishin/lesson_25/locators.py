from selenium.webdriver.common.by import By


class QaPractLocators:
    TEXT_INPUT = (By.XPATH, '//*[@name="text_string"]')
    RESULT_TEXT = (By.XPATH, '//*[@id="result-text"]')

    LANGUAGE_SELECTOR = (By.XPATH, '//*[@name="choose_language"]')


class ToolsQaLocators:
    REGISTRATION_FORM = (By.XPATH, '//*[@id="userForm"]')

    FIRSTNAME_INPUT = (By.XPATH, '//*[@id="firstName"]')
    LASTNAME_INPUT = (By.XPATH, '//*[@id="lastName"]')
    GENDER = (By.XPATH, '//*[@name="gender"]')
    EMAIL_INPUT = (By.XPATH, '//*[@id="userEmail"]')
    PHONE_INPUT = (By.XPATH, '//*[@id="userNumber"]')
    SUBJECTS = (By.XPATH, '//*[@id="subjectsInput"]')
    HOBBIES = (By.XPATH, '//*[contains(@id, "hobbies-checkbox")]')
    CURRENT_ADDRESS = (By.XPATH, '//*[@id="currentAddress"]')
    STATE_SELECTOR = (By.XPATH, '//*[@id="state"]')
    CITY_SELECTOR = (By.XPATH, '//*[@id="city"]')

    BIRTHDAY_INPUT = (By.XPATH, '//*[@id="dateOfBirthInput"]')
    MONTH_SELECTOR = (By.XPATH, '//*[contains(@class, "month-select")]')
    YEAR_SELECTOR = (By.XPATH, '//*[contains(@class, "year-select")]')

    RESULT_TABLE = (By.XPATH, '//*[contains(@class, "table-dark")]')

    @staticmethod
    def select_day(day):
        return (By.XPATH, f'//*[@role="option" and text()="{day}"]')


class HerokuAppLocators:
    START_BUTTON = (By.XPATH, '//*[text()="Start"]')
    HELLO_WORLD = (By.XPATH, '//*[@id="finish"]')
