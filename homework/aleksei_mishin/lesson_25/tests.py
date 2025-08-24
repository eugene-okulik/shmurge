import allure
import pytest
import random
from selenium import webdriver
from pages import InputsPage, StudentRegistrationPage, HerokuAppPage
from data_test import OtherTestData

QA_PRACTICE_INPUTS_LINK = 'https://www.qa-practice.com/elements/input/simple'
QA_PRACTICE_SELECTS_LINK = 'https://www.qa-practice.com/elements/select/single_select'
DEMO_QA_REGISTRATION_LINK = ' https://demoqa.com/automation-practice-form'
HEROKUAPP_LINK = 'https://the-internet.herokuapp.com/dynamic_loading/2'


@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver
    driver.close()


@allure.title('Тест: заполнения инпута')
def test_exercise_1(browser):
    page = InputsPage(browser, QA_PRACTICE_INPUTS_LINK)
    page.open()
    exp_res = page.text_input.fill_input(OtherTestData.word_en)
    page.text_input.submit()

    page.text_should_be_correct(exp_res)


@allure.title('Тест: заполнение формы регистрации студента')
def test_exercise_2(browser):
    page = StudentRegistrationPage(browser, DEMO_QA_REGISTRATION_LINK)
    page.open()
    page.fill_registration_form()
    page.registration_form.submit()

    page.print_result()


@allure.title('Тест: выбор языка программирования в дропдауне')
def test_exercise_3_1(browser):
    page = InputsPage(browser, QA_PRACTICE_SELECTS_LINK)
    page.open()
    exp_res = page.language_selector.select_by_text(random.choice(OtherTestData.code_languages))
    page.language_selector.submit()

    page.text_should_be_correct(exp_res)


@allure.title('Тест: нажатие кнопки Start')
def test_exercise_3_2(browser):
    page = HerokuAppPage(browser, HEROKUAPP_LINK)
    page.open()
    page.start_button.click()

    page.should_be_hello_world()
