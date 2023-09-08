from base.seleniumbase import SeleniumBase
from selenium.webdriver.common.by import By
import allure


class YmPage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self._ym = ("xpath", "//*[contains(text(), '40023215')]")
        self._catalog = (By.CSS_SELECTOR, "[data-id='182']")
        self._stroymaterialy = (By.CSS_SELECTOR, "[data-id='785']")
        self._product = (By.CSS_SELECTOR, ".pc-link")
        self._btn = (By.CSS_SELECTOR, ".add-to-cart.yellow-btn")

    @allure.step("Проверяем что метрика 40023215 представлена на странице")
    def get_ym(self):
        return self.element_is_present(self._ym)

    @allure.step("Проверяем что блок 'Стройматериалы' виден на странице")
    def get_catalog(self):
        return self.element_is_clickable(self._catalog)

    @allure.step("Проверяем кликабельность первой ссылки каталога на странице")
    def get_stroymaterialy(self):
        return self.element_is_clickable(self._stroymaterialy)

    @allure.step("Выбираем первый элемент каталога на странице")
    def get_product(self):
        return self.element_is_clickable(self._product)

    @allure.step("Проверяем у товара кликабельность кнопки 'В корзину'")
    def get_btn(self):
        return self.element_is_present(self._btn)
