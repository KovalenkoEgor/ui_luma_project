from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.enums.global_enums import GlobalErrorText
import allure


class BasePage:
    BASE_URL = 'https://magento.softwaretestingboard.com/'
    PAGE_URL = None

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 6)

    @allure.step("Open page")
    def open_page(self):
        if self.PAGE_URL:
            self.driver.get(f'{self.BASE_URL}{self.PAGE_URL}')
        else:
            raise NotImplementedError('Page cannot be opened for this class')

    @allure.step("Find a locator")
    def find(self, locator: tuple):
        return self.driver.find_element(*locator)

    @allure.step("Check element is displayed")
    def element_is_displayed(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Check current URL")
    def current_url_is_(self, url):
        assert self.driver.current_url == url, GlobalErrorText.WRONG_URL.value

    @allure.step("Check elemnet is clickable")
    def element_is_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))
