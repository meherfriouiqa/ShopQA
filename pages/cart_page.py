from pages.base_page import BasePage
from utils.locators import *
from time import sleep

class CartPage(BasePage):

    def __init__(self, driver):
        self.locator = CartPageLocators
        super().__init__(driver)  # Python3 version


    def run_cart(self):
        # check value inside cart
        isCartHaveValue =self.getText(locator=self.locator.CHECK_VALUE,locatorType="xpath")
        if isCartHaveValue !="":
            print("Already Item in the Cart")
        else:
            print('Make sure to add Item to the cart')
        sleep(4)
        # Total Value
        total_value =self.getText(locator=self.locator.CHECK_TOTAL_VALUE,locatorType="xpath")
        if total_value !="":
            print("The Total is ",total_value)
        else:
            print('No Total Value')
        sleep(2)
        self.elementClick(locator=self.locator.BTN_PROCEED, locatorType="xpath")
        sleep(2)
        
        
        
        
        