import pytest
from pages.basket_page import BasketPage
from pages.item_page import ItemPage
from pages.main_page import MainPage


@pytest.fixture(scope='function', autouse=True)
def setup(driver):
    main_page = MainPage(driver)
    item_page = ItemPage(driver)
    basket_page = BasketPage(driver)
    yield main_page, item_page, basket_page


@pytest.fixture
def main_page(driver, url):
    page = MainPage(driver)
    driver.get(url)
    return page
