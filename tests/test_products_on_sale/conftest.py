import pytest
from constants import MAIN_PAGE_STAGE_URL
from pages.products_on_sale_page import ProductsOnSale


@pytest.fixture(scope='function')
def product_page_open(driver, link):
    """Открывает страницу каталога по link"""
    if MAIN_PAGE_STAGE_URL in link:
        driver.get("https://dev:123456@test2.stroyrem-nn.ru/")
    page = ProductsOnSale(driver)
    driver.get(link)
    return page
