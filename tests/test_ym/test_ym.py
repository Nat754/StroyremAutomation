import pytest
import allure
from constants import MAIN_PAGE_PROD_URL
from .ym_constants import URLS_FOR_YM
from pages.ym_page import YmPage


@allure.epic("YA Metric")
class TestYaMetric:

    @allure.title("ym_is_present_smoke")
    @pytest.mark.parametrize('link', URLS_FOR_YM)
    @pytest.mark.smoke_test
    def test_ym_is_present_smoke(self, driver, link):
        page = YmPage(driver)
        driver.get(link)
        ya_metric = page.get_ym().is_enabled()
        assert ya_metric is True, f'Нет Яндекс метрики'

    @allure.title("ym_is_present_smoke")
    @pytest.mark.smoke_test
    def test_ym_is_present_on_product_card_smoke(self, driver):
        page = YmPage(driver)
        driver.get(MAIN_PAGE_PROD_URL)
        page.get_catalog().click()
        page.get_stroymaterialy().click()
        page.get_product().click()
        page.get_btn().click()
        ya_metric = page.get_ym().is_enabled()
        assert ya_metric is True, f'Нет Яндекс метрики'
