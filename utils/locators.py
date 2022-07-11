from selenium.webdriver.common.by import By


# for maintainability we can seperate web objects by page name

class MainPageLocators(object):
    HOME_PAGE = '//*[@id="slide-6-layer-3"]'
    ARTICLE='//*[@id="noo-site"]/div[2]/div[4]/div/div[1]/div/div/div/div[2]/div[2]/div[1]'


class ProductPageLocators(object):
    SELECT_PRODUCT="//select[@id='color']"
    SELECT_WHILE_PRODUCT="//select[@id='color']/option[@value='White']"
    SELECT_PRODUCT_SIZE="//select[@id='size']"
    SELECT_PRODUCT_SIZE_LARGE="//select[@id='size']/option[@value='L']"
    CLICK_ADD_BUTTON="//button[@class='single_add_to_cart_button button alt']"
    SUCCESS_MESSAGE='//*[@id="noo-site"]/div[2]/div/div/div[1]/div'
    VIEW_CART="//a[text()='View cart']"


class CartPageLocators(object):
    CHECK_VALUE='//*[@id="nav-menu-item-cart"]/a/span'
    CHECK_TOTAL_VALUE='//*[@id="nav-menu-item-cart"]/a/span/span[2]/span/bdi'
    BTN_PROCEED='//*[@id="post-6"]/div/div/div[2]/div[2]/div/a'


class CheckOutPageLocators(object):
    CHECKOUT_PAGE='//h1[text()="Checkout"]'
    FIRST_NAME="billing_first_name"
    LAST_NAME="billing_last_name"
    SELECT_COUNTRY='//*[@id="billing_country_field"]/span/span/span[1]/span'
    COUNTRY_NAME="//input[@class='select2-search__field']"
    SELECT_COUNTRY_TUNISIA='//li[text()="Tunisia"]'
    ENTER_STREET_ADDRESS="billing_address_1"
    ENTER_CITY="billing_city"
    ENTER_STATE="billing_state"
    ENTER_CODE_POSTAL="billing_postcode"
    ENTER_PHONE="billing_phone"
    ENTER_EMAIL="billing_email"
    CLICK_AGREE="//input[@id='terms']"
    BTN_ORDER="//button[text()='Place order']"
    MESSAGE_SUCCESS="//p[text()='Thank you. Your order has been received.']"