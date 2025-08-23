from selenium.webdriver.common.by import By


class MainPageLocators:
    GOODS = (By.XPATH, '//*[contains(@class, "oe_product_image_link ")]')
    CART_BUTTON = (By.XPATH, '//*[contains(@class, "navbar-nav align")]/child::li[2]')


class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.XPATH, '//*[@id="add_to_cart"]')
    PRODUCT_TITLE = (By.XPATH, '//*[@class="breadcrumb-item active"]')

    MODAL_WINDOW = (By.XPATH, '//*[@class="modal-content"]')
    MODAL_WINDOW_CONTINUE_SHOPPING = (By.XPATH, '//*[@class="btn btn-secondary"]')
    MODAL_WINDOW_PRODUCT_NAME = (By.XPATH, '//*[@class="td-product_name"]/child::strong')


class CartPageLocators:
    PRODUCT_TITLE = (By.XPATH, '//*[contains(@class, "d-inline align-top")]')


class MagentoPageLocators:
    GOODS = (By.XPATH, '//*[@class="product name product-item-name"]')
    ADD_TO_COMPARE_BUTTONS = (By.XPATH, '//*[@class="action tocompare"]')
    COMPARE_ITEM_QUANTITY = (By.XPATH, '//*[@class="action compare"]/child::span')
