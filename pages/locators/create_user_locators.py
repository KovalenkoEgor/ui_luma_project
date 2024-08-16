from selenium.webdriver.common.by import By

first_name_loc = (By.ID, 'firstname')
second_name_loc = (By.ID, 'lastname')
email_loc = (By.ID, 'email_address')
password_loc = (By.ID, 'password')
confirm_pass_loc = (By.ID, 'password-confirmation')
confirm_loc = (By.CSS_SELECTOR, '[class="action submit primary"]')
thank_text_loc = (By.XPATH, '//*[text()="Thank you for registering with Main '
                            'Website Store."]')
first_name_error_text_loc = (By.ID, 'firstname-error')
error_message_text_loc = (By.XPATH, '//div[@id="email_address-error"]')
box_content_loc = (By.XPATH, '//div[@class="box-content"]')

message_loc = (By.XPATH, '(//div[@class="messages"])[1]')
