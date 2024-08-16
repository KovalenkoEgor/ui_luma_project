import pytest
from utils.project_ec import (ru_first_name, en_first_name, ru_last_name, en_last_name, ru_email, en_email,
                              ru_password_field, en_password_field, ru_confirm_pass, en_confirm_pass, wrong_email,
                              empty_name)


@pytest.mark.parametrize(
    'data',
    [
        pytest.param((ru_first_name, ru_last_name, ru_email, ru_password_field, ru_confirm_pass)),
        pytest.param((en_first_name, en_last_name, en_email, en_password_field, en_confirm_pass))
    ]
)
def test_fill_form_correctly(customer_page, data):
    first_name, last_name, email, password, con_password = data
    customer_page.open_page()
    customer_page.create_new_account(first_name, last_name, email, password, con_password)
    customer_page.click_confirm()
    customer_page.check_successful_created_account_text_is_('Thank you for registering with Main Website Store.')


def test_input_name_is_correct(customer_page):
    customer_page.open_page()
    customer_page.create_new_account(ru_first_name, ru_last_name, ru_email, ru_password_field, ru_confirm_pass)
    customer_page.click_confirm()
    customer_page.input_name_is_correct(ru_first_name)


def test_first_name_is_empty_error_message(customer_page):
    customer_page.open_page()
    customer_page.create_new_account(empty_name, en_last_name, en_email, en_password_field, en_confirm_pass)
    customer_page.click_confirm()
    customer_page.check_first_name_error_text_is_('This is a required field.')


def test_dog_is_presented_in_email(customer_page):
    customer_page.open_page()
    customer_page.create_new_account(en_first_name, en_last_name, en_email, en_password_field, en_confirm_pass)
    customer_page.dog_symbol_is_present(en_email)
    customer_page.click_confirm()


def test_email_is_invalid(customer_page):
    customer_page.open_page()
    customer_page.create_new_account(en_first_name, en_last_name, wrong_email, en_password_field, en_confirm_pass)
    customer_page.click_confirm()
    customer_page.is_invalid_email_error('Please enter a valid email address (Ex: johndoe@domain.com).')
