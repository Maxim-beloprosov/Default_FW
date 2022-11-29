import allure
from selenium.webdriver.common.by import By

from fw.web.AnyPage import AnyPage


class Locator:
    cke_contents = (By.CSS_SELECTOR, '[test_id="guide-others"] svg')
    button_custom_field_dictionary = (By.CSS_SELECTOR, '[test_id="guide-others"] svg')


class CatalogueWeb(AnyPage):

    def page_loaded(self):
        """
        Ждем появления элементов страницы
        """
        self.find_element(Locator.cke_contents)

    @allure.step('Переход к пользовательским справочникам')
    def switching_to_custom_field_dictionaries(self):
        self.click_element(Locator.button_custom_field_dictionary)
        return self
