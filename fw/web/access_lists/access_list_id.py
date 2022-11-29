from selenium.webdriver.common.by import By
import allure
from fw.web.AnyPage import AnyPage


class Locator:
    page_loaded = (By.XPATH, '//div[@class="acl-list"]')


class AccessListId(AnyPage):

    def page_loaded(self):
        """
        Ждем появления элементов страницы
        """
        self.find_element(Locator.page_loaded)


