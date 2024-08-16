from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import create_user_locators as loc
from utils.enums.global_enums import GlobalErrorText


class CustomerAccount(BasePage):
    PAGE_URL = '/customer/account/create'

    def create_new_account(self, first_name, last_name, email, password, confirm_pass):
        first_name_field = self.find(loc.first_name_loc)
        second_name_field = self.find(loc.second_name_loc)
        email_field = self.find(loc.email_loc)
        password_field = self.find(loc.password_loc)
        confirm_password_field = self.find(loc.confirm_pass_loc)

        first_name_field.send_keys(first_name)
        second_name_field.send_keys(last_name)
        email_field.send_keys(email)
        password_field.send_keys(password)
        confirm_password_field.send_keys(confirm_pass)

    def click_confirm(self):
        confirm_button = self.find(loc.confirm_loc)
        confirm_button.click()

    def check_successful_created_account_text_is_(self, text):
        wait = WebDriverWait(self.driver, 6)
        thank_text = wait.until(
            EC.visibility_of_element_located(loc.thank_text_loc))
        assert thank_text.text == text

    def check_first_name_error_text_is_(self, text):
        wait = WebDriverWait(self.driver, 6)
        first_name_error_text = wait.until(EC.visibility_of_element_located(loc.first_name_error_text_loc))
        assert first_name_error_text.text == text

    def is_invalid_email_error(self, text):
        error_message_text = self.find(loc.error_message_text_loc)
        assert error_message_text.text == text

    def dog_symbol_is_present(self, email_field):
        assert '@' in email_field

    def input_name_is_correct(self, name):
        wait = WebDriverWait(self.driver, 6)
        contact_name = wait.until(EC.presence_of_element_located(loc.box_content_loc))
        assert contact_name.text.split()[0] == name, GlobalErrorText.WRONG_NAME.value
