from selenium.webdriver.common.by import By
import allure
from fw.web.AnyPage import AnyPage


class Locator:
    page_loaded = (By.XPATH, '//div[@class="acl-list"]')
    create_access_list_todo = (By.XPATH, '//button[@test_id="ac-button-create"]')


class AccessListsWEB(AnyPage):

    def page_loaded(self):
        """
        Ждем появления элементов страницы
        """
        self.find_element(Locator.page_loaded)

    @allure.step('Нажимаем на кнопку Создать лист допуска')
    def button_to_create_access_list(self):
        self.click_element(Locator.create_access_list_todo)
        self.manager.web_access_list_create.page_loaded()
        return self.manager.web_access_list_create

    @allure.step('Проверяем, есть ли кнопка создания листа допуска на странице')
    def check_is_there_button_create_access_list_on_the_page(self):
        button_create_access_list = self.check_is_there_element_on_the_page(Locator.create_access_list_todo)
        return button_create_access_list

    @allure.step('Проверяем, есть ли кнопка создания листа допуска на странице')
    def check_is_there_button_create_access_list_on_the_page(self):
        button_create_access_list = self.check_is_there_element_on_the_page(Locator.create_access_list_todo)
        return button_create_access_list



