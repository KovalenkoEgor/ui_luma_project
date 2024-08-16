from pages.base_page import BasePage
from utils.enums.global_enums import GlobalErrorText
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import eco_friendly_locators as loc
# from selenium.webdriver.common.alert import Alert


class EcoCollections(BasePage):
    PAGE_URL = '/collections/eco-friendly.html'

    def add_shorts_to_a_card(self):
        wait = WebDriverWait(self.driver, 5)
        ana_shorts_button = self.find(loc.ana_running_loc)
        ana_shorts_button.click()

        size_choose_button = wait.until(EC.visibility_of_element_located(loc.option_label_size_29_loc))
        size_choose_button.click()

        color_choose_button = self.find(loc.option_label_color_orange_loc)
        color_choose_button.click()

        qty_button = self.find(loc.input_qty_loc)
        qty_button.clear()
        qty_button.send_keys('2')

    def action_submit(self):
        cart_button = self.find(loc.submit_cart_loc)
        cart_button.click()

    def click_mini_cart(self):
        wait = WebDriverWait(self.driver, 6)
        wait.until(EC.element_to_be_clickable(loc.mini_cart_loc)).click()

    def check_product_name_in_cart_is_(self, name):
        wait = WebDriverWait(self.driver, 6)
        wait.until(EC.element_to_be_clickable(loc.mini_cart_loc)).click()
        anna_short_text = self.find(loc.anna_short_loc)
        assert anna_short_text.text == name, GlobalErrorText.WRONG_NAME.value

    def remove_items_from_cart(self):
        wait = WebDriverWait(self.driver, 6)
        wait.until(EC.element_to_be_clickable(loc.mini_cart_loc)).click()
        remove_item = self.find(loc.remove_item_loc)
        remove_item.click()
        self.find(loc.button_accept_loc).click()
        # alert = wait.until(EC.alert_is_present())
        # alert.accept()

    def check_text_in_empty_cart_is_(self, text):
        empty_cart = self.find(loc.empty_cart_text_loc)
        assert empty_cart.text == text

    def proceed_to_shipping(self):
        wait = WebDriverWait(self.driver, 6)
        wait.until(EC.element_to_be_clickable(loc.mini_cart_loc)).click()
        proceed_button = self.find(loc.proceed_loc)
        proceed_button.click()

    def redirect_to_new_shipping_url_address(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.url_changes('https://magento.softwaretestingboard.com/checkout/#shipping'))

    def warning_text_is_(self, text):
        wait = WebDriverWait(self.driver, 10)
        warning_message = wait.until(EC.presence_of_element_located(loc.warning_text_loc))
        assert warning_message.text == text
