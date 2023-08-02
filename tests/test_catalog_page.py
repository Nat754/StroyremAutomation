import pytest
import allure
from tests.catalog.conftest import catalog_page_open
from constants import MAIN_PAGE_STAGE_URL, MAIN_PAGE_PROD_URL


@allure.epic("Catalog Page")
class TestCatalogPage:

    @allure.title("001_positive_button_stroymateriali_smoke(catalog)")
    @pytest.mark.parametrize('link', [MAIN_PAGE_PROD_URL, MAIN_PAGE_STAGE_URL])
    @pytest.mark.smoke_test
    def test_001_positive_button_stroymateriali_smoke_catalog(self, driver, link, catalog_page_open):
        catalog_page_open.get_catalog_stroymateriali_link().click()
        assert catalog_page_open.get_catalog_stroymateriali_text().text == "Стройматериалы", \
            "Меню 'Стройматериалы' не отображается"
        assert catalog_page_open.get_navigation_glavnaya_catalog_text()[0].text == "Главная", \
            "Меню навигации 'Главная' не отображается"
        assert catalog_page_open.get_navigation_glavnaya_catalog_text()[1].text == "Каталог", \
            "Меню навигации 'Каталог' не отображается"
