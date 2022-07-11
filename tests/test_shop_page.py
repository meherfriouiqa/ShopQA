import unittest
from tests.base_test import BaseTest
from pages.home_page import *
from pages.product_page import *
from pages.cart_page import *
from pages.checkout_page import *

from utils.test_cases import test_cases
from time import sleep


# I am using python unittest for asserting cases.
# In this module, there should be test cases.
# If you want to run it, you should type: python <module-name.py>

class TestShopPage(BaseTest):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locator = MainPageLocators

    def test_page_shop(self):
        page = HomePage(self.driver)
        page.runshopsenario()
        product=ProductPage(self.driver)
        product.run_product()
        cart=CartPage(self.driver)
        cart.run_cart()
        checkout=CheckOutPage(self.driver)
        checkout.run_checkout()

        
        