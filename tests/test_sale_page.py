from pages.locators import sale_page_locators as loc


def test_title_name_is_correct(sale_page):
    sale_page.open_page()
    sale_page.title_text_is('Sale')


def test_current_url_is_correct(sale_page):
    sale_page.open_page()
    sale_page.current_url_is_('https://magento.softwaretestingboard.com//sale.html')


def test_current_url(sale_page):
    sale_page.open_page()
    sale_page.element_is_displayed(loc.base_title_loc)


def test_element_is_clickable(sale_page):
    sale_page.open_page()
    sale_page.element_is_clickable(loc.jacket_loc)
