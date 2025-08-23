import allure
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from elements import Button
from locators import MainPageLocators, ProductPageLocators, CartPageLocators, MagentoPageLocators


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        with allure.step(f'Открыть страницу: {self.url}'):
            return self.browser.get(self.url)

    def open_link_in_new_tab(self, element):
        with allure.step('Открыть в новой вкладке'):
            action = AC(self.browser)
            action.key_down(Keys.COMMAND)
            action.click(element)
            action.key_up(Keys.COMMAND)
            action.perform()

    def switch_to_new_tab(self):
        tabs = self.browser.window_handles
        self.browser.switch_to.window(tabs[1])

    def switch_to_previous_tab(self):
        tabs = self.browser.window_handles
        self.browser.switch_to.window(tabs[0])

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

    def should_be_correct_page(self, path):
        assert path in self.browser.current_url, (f'Некорректный URL!'
                                                  f'URL должен содержать "{path}"'
                                                  f'Текущий URL: {self.browser.current_url}')


class MainPage(BasePage):

    def __init__(self, browser, url):
        super().__init__(browser, url)

        self.goods = Button(self.browser, 'Товары', *MainPageLocators.GOODS)
        self.cart_button = Button(self.browser, 'Корзина', *MainPageLocators.CART_BUTTON)

    def open_product_link_in_new_tab(self):
        goods = self.goods.get_elements()
        self.open_link_in_new_tab(goods[0])
        self.switch_to_new_tab()
        self.should_be_correct_page('shop')

    def go_to_cart(self):
        self.cart_button.click()
        self.should_be_correct_page('cart')


class ProductPage(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)

        self.add_to_cart_button = Button(
            self.browser,
            'Добавить в корзину',
            *ProductPageLocators.ADD_TO_CART_BUTTON
        )
        self.continue_shopping = Button(
            self.browser,
            'Продолжить покупки',
            *ProductPageLocators.MODAL_WINDOW_CONTINUE_SHOPPING
        )
        self.verbose_product_name_in_modal = Button(
            self.browser,
            'Наименование товара в модальном окне',
            *ProductPageLocators.MODAL_WINDOW_PRODUCT_NAME
        )
        self.product_name = Button(self.browser, 'Наименование товара', *ProductPageLocators.PRODUCT_TITLE)

    def add_product_to_cart(self):
        self.add_to_cart_button.click()

    def continue_shopping_in_modal(self):
        self.continue_shopping.click()

    def get_product_name_from_modal(self):
        return self.verbose_product_name_in_modal.get_text_of_element()


class CartPage(BasePage):

    def __init__(self, browser, url):
        super().__init__(browser, url)

        self.product_title = Button(self.browser, 'Наименование товара', *CartPageLocators.PRODUCT_TITLE)

    def check_product_in_cart(self, exp_res):
        act_res = self.product_title.get_text_of_element()
        assert act_res in exp_res, (f'Товар не найден в корзине!\n'
                                    f'Полное наименование товара {exp_res}\n'
                                    f'Должно содержать {act_res}')


class MagentoPage(BasePage):

    def __init__(self, browser, url):
        super().__init__(browser, url)

        self.bags = Button(self.browser, 'Сумки', *MagentoPageLocators.GOODS)
        self.add_to_compare_buttons = Button(
            self.browser,
            'Кнопка: Сравнить',
            *MagentoPageLocators.ADD_TO_COMPARE_BUTTONS
        )
        self.compare_item_quantity = Button(
            self.browser,
            'Количество товаров для сравнения',
            *MagentoPageLocators.COMPARE_ITEM_QUANTITY
        )

    def add_product_to_compare(self, index=0):
        product = self.bags.get_elements()[index]
        add_to_compare = self.add_to_compare_buttons.get_elements()[index]
        self.bags.scroll_to_element(product)
        self.bags.move_to_element(product)
        self.add_to_compare_buttons.move_to_element(add_to_compare)
        self.add_to_compare_buttons.click(add_to_compare)

    def should_be_correct_quantity_items_to_compare(self, exp_res: int):
        act_res = self.compare_item_quantity.get_text_of_element().split()
        act_res = int(act_res[0])
        assert act_res == exp_res, (f'Некорректное количество товаров для сравнения!\n'
                                    f'ОР: {exp_res}\n'
                                    f'ФР: {act_res}')
