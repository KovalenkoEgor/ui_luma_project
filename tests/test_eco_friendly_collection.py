def test_product_name_in_cart_is_correct(collection_page):
    collection_page.open_page()
    collection_page.add_shorts_to_a_card()
    collection_page.action_submit()
    collection_page.click_mini_cart()
    collection_page.check_product_name_in_cart_is_('Ana Running Short')


def test_remove_items_from_cart(collection_page):
    collection_page.open_page()
    collection_page.add_shorts_to_a_card()
    collection_page.action_submit()
    collection_page.click_mini_cart()
    collection_page.remove_items_from_cart()
    collection_page.check_text_in_empty_cart_is_('You have no items in your shopping cart.')


def test_proceed_to_checkout_message(collection_page):
    collection_page.open_page()
    collection_page.add_shorts_to_a_card()
    collection_page.action_submit()
    collection_page.click_mini_cart()
    collection_page.proceed_to_shipping()
    collection_page.redirect_to_new_shipping_url_address()
    collection_page.warning_text_is_('This is a demo store to test your test automaiton scripts. No orders will be '
                                     'fulfilled. If you are facing any issue, email us at '
                                     'hello@softwaretestingboard.com.')
