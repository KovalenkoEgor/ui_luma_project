from selenium import webdriver
import pytest
from pages.create_new_account import CustomerAccount
from pages.eco_friendly_page import EcoCollections
from pages.sale_page import SalePage


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    chrome_driver.implicitly_wait(5)
    return chrome_driver


@pytest.fixture()
def customer_page(driver):
    return CustomerAccount(driver)


@pytest.fixture()
def collection_page(driver):
    return EcoCollections(driver)


@pytest.fixture()
def sale_page(driver):
    return SalePage(driver)
