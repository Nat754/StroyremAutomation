import pytest

from constants import MAIN_PAGE_STAGE_URL
from pages.catalog_page import CatalogPage


@pytest.fixture(scope='function')
def catalog_page_open(driver, link):
    if MAIN_PAGE_STAGE_URL in link:
        driver.get("https://dev:123456@test2.stroyrem-nn.ru/")
    catalog_page = CatalogPage(driver)
    driver.get(link)
    catalog_page.get_header_catalog_menu().click()
    return catalog_page
