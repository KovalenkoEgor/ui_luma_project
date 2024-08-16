from pages.base_page import BasePage
from pages.locators import sale_page_locators as loc


class SalePage(BasePage):
    PAGE_URL = '/sale.html'

    def title_text_is(self, text):
        element = self.find(loc.base_title_loc)
        assert element.text == text
