from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    BASE_URL = 'https://magento.softwaretestingboard.com/'
    PAGE_URL = None

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_page(self):
        if self.PAGE_URL:
            self.driver.get(f'{self.BASE_URL}{self.PAGE_URL}')
        else:
            raise NotImplementedError('Page cannot be opened for this class')

    def find(self, locator: tuple):
        return self.driver.find_element(*locator)

    def element_is_displayed(self, locator):
        title = self.find(locator)
        assert title.is_displayed()

    def current_url_is_(self, url):
        assert self.driver.current_url == url

    def element_is_clickable(self, locator):
        WebDriverWait(self.driver, 4).until(
            EC.element_to_be_clickable(locator))
