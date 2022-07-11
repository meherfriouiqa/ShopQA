from pages.base_page import BasePage
from utils.locators import *
from time import sleep

class HomePage(BasePage):

    def __init__(self, driver):
        self.locator = MainPageLocators
        super().__init__(driver)  # Python3 version

    
    def choose_article(self):
        self.elementClick(locator=self.locator.ARTICLE, locatorType="xpath")
    

    def runshopsenario(self):
        messageElement = self.waitForElement(self.locator.HOME_PAGE, locatorType="xpath")
        result = self.isElementDisplayed(element=messageElement)
        if result:
            self.webScroll(direction='down')
            sleep(2)
            self.choose_article()

        
        
