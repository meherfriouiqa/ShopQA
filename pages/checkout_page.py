from pages.base_page import BasePage
from utils.locators import *
from time import sleep

class CheckOutPage(BasePage):

    def __init__(self, driver):
        self.locator = CheckOutPageLocators
        super().__init__(driver)  # Python3 version


    def run_checkout(self):
        # check page checkout.
        checkoutPage =self.getText(locator=self.locator.CHECKOUT_PAGE,locatorType="xpath")
        assert checkoutPage=="CHECKOUT"
        sleep(2)
        # Enter First Name
        self.sendKeys("TECHNICAL",locator=self.locator.FIRST_NAME, locatorType="id")
        sleep(2)
        # Enter Last Name
        self.sendKeys("TEST",locator=self.locator.LAST_NAME, locatorType="id")
        sleep(2)
        self.elementClick(locator=self.locator.SELECT_COUNTRY, locatorType="xpath")
        sleep(2)
        self.sendKeys("TEST",locator=self.locator.COUNTRY_NAME, locatorType="id")
        sleep(2)
        self.elementClick(locator=self.locator.SELECT_COUNTRY_TUNISIA, locatorType="xpath")
        sleep(2)
        self.sendKeys("Tunis",locator=self.locator.ENTER_STREET_ADDRESS, locatorType="id")
        sleep(2)
        self.sendKeys("Tunis",locator=self.locator.ENTER_CITY, locatorType="id")
        sleep(2)
        self.sendKeys("Tunis",locator=self.locator.ENTER_STATE, locatorType="id")
        sleep(2)
        self.sendKeys("12345",locator=self.locator.ENTER_CODE_POSTAL, locatorType="id")
        sleep(2)
        self.sendKeys("23456789",locator=self.locator.ENTER_PHONE, locatorType="id")
        sleep(2)
        self.sendKeys("meherfriouiqa@gmail.com",locator=self.locator.ENTER_EMAIL, locatorType="id")
        sleep(2)
        self.elementClick(locator=self.locator.CLICK_AGREE, locatorType="xpath")
        sleep(2)
        self.elementClick(locator=self.locator.BTN_ORDER, locatorType="xpath")
        sleep(2)
        success_order =self.getText(locator=self.locator.MESSAGE_SUCCESS,locatorType="xpath")
        assert success_order=="Thank you. Your order has been received."
        sleep(2)
        


        





        

        
        
        
        
        
        