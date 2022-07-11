from pages.base_page import BasePage
from utils.locators import *
from time import sleep

class ProductPage(BasePage):

    def __init__(self, driver):
        self.locator = ProductPageLocators
        super().__init__(driver)  # Python3 version


    def run_product(self):
        # scroll the page in the middle of the page
        self.webScroll(direction='down')
        # slect product color
        isSelectProductPresent = self.waitForElement(self.locator.SELECT_PRODUCT, locatorType="xpath")
        result = self.isElementDisplayed(element=isSelectProductPresent)
        if result:
            self.elementClick(locator=self.locator.SELECT_PRODUCT, locatorType="xpath")
            sleep(1)
        # select white color product
        isSelectProductColorPresent = self.waitForElement(self.locator.SELECT_WHILE_PRODUCT, locatorType="xpath")
        result = self.isElementDisplayed(element=isSelectProductColorPresent)
        if isSelectProductColorPresent:
            self.elementClick(locator=self.locator.SELECT_WHILE_PRODUCT, locatorType="xpath")
            sleep(1)
        # select size
        iseSlectProductSizePresent = self.waitForElement(self.locator.SELECT_PRODUCT_SIZE, locatorType="xpath")
        result = self.isElementDisplayed(element=iseSlectProductSizePresent)
        if iseSlectProductSizePresent:
            self.elementClick(locator=self.locator.SELECT_PRODUCT_SIZE, locatorType="xpath")
            sleep(2)
        # select large size
        iseSlectProductSizeSmallPresent = self.waitForElement(self.locator.SELECT_PRODUCT_SIZE_LARGE, locatorType="xpath")
        result = self.isElementDisplayed(element=iseSlectProductSizeSmallPresent)
        if iseSlectProductSizeSmallPresent:
            self.elementClick(locator=self.locator.SELECT_PRODUCT_SIZE_LARGE, locatorType="xpath")
            sleep(2)
        # click on button Add 
        self.elementClick(locator=self.locator.CLICK_ADD_BUTTON, locatorType="xpath")
        sleep(2)
        # check success product add to the cart
        product_success=self.getText(locator=self.locator.SUCCESS_MESSAGE,locatorType="xpath").split('\n')[1]
        assert product_success =="“Tokyo Talkies” has been added to your cart."
        sleep(2)
        # Click on button view cart
        self.elementClick(locator=self.locator.VIEW_CART, locatorType="xpath")
        sleep(2)

        

        
      

        

