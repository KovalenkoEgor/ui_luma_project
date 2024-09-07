import pytest
from utils import project_ec as data


@pytest.mark.parametrize(
    'test_data',
    [
        pytest.param(
            (data.ru_first_name,
             data.ru_last_name, data.ru_email, data.ru_password_field, data.ru_confirm_pass)),
        pytest.param(
            (data.en_first_name, data.en_last_name, data.en_email, data.en_password_field, data.en_confirm_pass))
    ]
)
def test_fill_form_correctly(customer_page, test_data):
    first_name, last_name, email, password, con_password = test_data
    customer_page.open_page()
    customer_page.create_new_account(first_name, last_name, email, password, con_password)
    customer_page.click_confirm()
    customer_page.check_successful_created_account_text_is_('Thank you for registering with Main Website Store.')


def test_input_name_is_correct(customer_page):
    customer_page.open_page()
    customer_page.create_new_account(
        data.ru_first_name,
        data.ru_last_name,
        data.ru_email,
        data.ru_password_field,
        data.ru_confirm_pass
    )
    customer_page.click_confirm()
    customer_page.input_name_is_correct(data.ru_first_name)


def test_first_name_is_empty_error_message(customer_page):
    customer_page.open_page()
    customer_page.create_new_account(
        data.empty_name, data.en_last_name,
        data.en_email,
        data.en_password_field,
        data.en_confirm_pass
    )
    customer_page.click_confirm()
    customer_page.check_first_name_error_text_is_('This is a required field.')


def test_dog_is_presented_in_email(customer_page):
    customer_page.open_page()
    customer_page.create_new_account(
        data.en_first_name,
        data.en_last_name,
        data.en_email,
        data.en_password_field,
        data.en_confirm_pass)
    customer_page.dog_symbol_is_present(data.en_email)
    customer_page.click_confirm()


def test_email_is_invalid(customer_page):
    customer_page.open_page()
    customer_page.create_new_account(
        data.en_first_name,
        data.en_last_name,
        data.wrong_email,
        data.en_password_field,
        data.en_confirm_pass)
    customer_page.click_confirm()
    customer_page.is_invalid_email_error('Please enter a valid email address (Ex: johndoe@domain.com).')
