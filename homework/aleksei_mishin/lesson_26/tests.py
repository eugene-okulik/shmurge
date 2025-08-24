import pytest
from selenium import webdriver
from homework.aleksei_mishin.lesson_26.pages import CartPage
from pages import MainPage, ProductPage, MagentoPage

BASE_URL = 'http://testshop.qa-practice.com/'
MAGENTO_LINK = 'https://magento.softwaretestingboard.com/gear/bags.html'


@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver
    driver.close()


def test_first(browser):
    main_page = MainPage(browser, BASE_URL)
    main_page.open()
    main_page.open_product_link_in_new_tab()

    prod_page = ProductPage(browser, browser.current_url)
    prod_page.add_product_to_cart()
    product_name = prod_page.get_product_name_from_modal()
    prod_page.continue_shopping_in_modal()
    prod_page.switch_to_previous_tab()

    main_page.go_to_cart()

    cart_page = CartPage(browser, browser.current_url)
    cart_page.check_product_in_cart(product_name)


def test_second(browser):
    page = MagentoPage(browser, MAGENTO_LINK)
    page.open()
    prod_title = page.add_product_to_compare()

    page.should_be_correct_prod_title_in_compare_section(prod_title)
