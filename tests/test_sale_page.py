
def test_title_name_is_correct(sale_page):
    sale_page.open_page()
    sale_page.check_title_is_presented()
    sale_page.title_text_is('Sale')


def test_current_url_is_correct(sale_page):
    sale_page.open_page()
    sale_page.current_url_is_('https://magento.softwaretestingboard.com//sale.html')


def test_element_is_clickable(sale_page):
    sale_page.open_page()
    sale_page.check_jacket_element_is_clickable()
