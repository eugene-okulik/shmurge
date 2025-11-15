import pytest

from test_UI_amishin_pw.pages.account_page import AccountPage
from test_UI_amishin_pw.pages.cart_page import CartPage
from test_UI_amishin_pw.pages.create_account_page import CreateAccountPage
from test_UI_amishin_pw.pages.header_page import HeaderPage
from test_UI_amishin_pw.pages.login_page import LoginPage
from test_UI_amishin_pw.pages.main_page import MainPage
from test_UI_amishin_pw.pages.modal_add_to_cart import ModalAddToCart
from test_UI_amishin_pw.pages.product_page import ProductPage


class BaseTest:
    account_page = AccountPage
    cart_page = CartPage
    create_account_page = CreateAccountPage
    header_page = HeaderPage
    login_page = LoginPage
    main_page = MainPage
    modal_add_to_cart = ModalAddToCart
    product_page = ProductPage

    @pytest.fixture(autouse=True)
    def setup(self, request, page):
        request.cls.page = page

        request.cls.account_page = AccountPage(page)
        request.cls.cart_page = CartPage(page)
        request.cls.create_account_page = CreateAccountPage(page)
        request.cls.header_page = HeaderPage(page)
        request.cls.login_page = LoginPage(page)
        request.cls.main_page = MainPage(page)
        request.cls.modal_add_to_cart = ModalAddToCart(page)
        request.cls.product_page = ProductPage(page)
