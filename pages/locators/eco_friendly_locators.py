from selenium.webdriver.common.by import By

ana_running_loc = (By.XPATH, '//img[@alt="Ana Running Short"]')
option_label_size_29_loc = (By.XPATH, '//div[@id="option-label-size-143-item-172"]')
option_label_color_orange_loc = (By.XPATH, '(//div[@id="option-label-color-93-item-56"])[1]')
input_qty_loc = (By.XPATH, '//input[@id="qty"]')
submit_cart_loc = (By.CSS_SELECTOR, '[class="action primary tocart"]')
mini_cart_loc = (By.XPATH, '//a[@class="action showcart"]')
anna_short_loc = (By.XPATH, '//a[text()="Ana Running Short"]')
remove_item_loc = (By.XPATH, '//a[@class="action delete"]')
empty_cart_text_loc = (By.XPATH, '//*[text()="You have no items in your shopping cart."]')
button_accept_loc = (By.XPATH, '//button[@class="action-primary action-accept"]')
proceed_loc = (By.XPATH, '//button[@id="top-cart-btn-checkout"]')
warning_text_loc = (By.XPATH, '(//div[@class="content"])[1]')
